import pathlib
import warnings
from datetime import date, datetime, timedelta
from enum import Enum
from typing import Optional, Type
from dateutil import parser
import dicttoxml
import json
import logging
import os
import platform
import uuid

from xmltv.models import *
from xmltv import xmltv_helpers
from xsdata.exceptions import ConverterError
from xsdata.formats.converter import Converter, converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.models.xsd import Any

from PlutoTV import ptvChannels
import urllib
from urllib.request import urlopen
from jinja2 import Template

dicttoxml.LOG.setLevel(logging.ERROR)

_URL_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
_NEW_DATE_FORMAT_NO_TZ = '%Y%m%d%H%M%S'


class PlutoTv:

    XML_PARSER = XmlParser(context=XmlContext())
    API_URL = 'https://api.pluto.tv'
    GUIDE_URL = '{}/v2/channels'.format(API_URL)

    config_dir = pathlib.Path('/config')
    data_out_dir = '/data/PlutoTV/'
    if os.path.exists(data_out_dir):
        m3u_file_name = data_out_dir + 'PlutoTV.m3u'
        xmltv_file_name = data_out_dir + 'PlutoTVGuide.xml'
    else:
        m3u_file_name = 'PlutoTV.m3u'
        xmltv_file_name = 'PlutoTV.xml'

    if os.path.exists(config_dir):
        log_file = config_dir / 'log' / 'PlutoTV.log'
    else:
        log_file = 'PlutoTV.log'

    LOGGER = logging.getLogger('PlutoTV-Logger')
    logging.basicConfig(format='%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s',
                        level=logging.getLevelName(os.getenv('LOG_LEVEL', 'ERROR')),
                        handlers=[logging.FileHandler(log_file),
                                  logging.StreamHandler()])

    CHANNELS: ptvChannels.Root
    TV_OBJECT: xmltv.Tv

    def main(self):
        _start_time = datetime.now().replace(minute=0, second=0, microsecond=0)
        _stop_time = _start_time + timedelta(days=2)
        _API_ARGS = {
            'start': self.get_proper_date_time(_start_time, _URL_TIME_FORMAT),
            'stop': self.get_proper_date_time(_stop_time, _URL_TIME_FORMAT),
            'appName': 'web',
            'appVersion': 'unknown',
            'appStoreUrl': 'unknown',
            'architecture': platform.machine(),
            'buildVersion': 'unknown',
            'clientTime': 0,
            'deviceDNT': 0,
            'deviceId': uuid.uuid1(),
            'deviceMake': 'Chrome',
            'deviceModel': 'web',
            'deviceType': 'web',
            'deviceVersion': 'unknown',
            'includeExtendedEvents': False,
            'sid': uuid.uuid4(),
            'userId': os.getenv('PLUTO_USER_ID', ''),
            'serverSideAds': True
        }

        self.GUIDE_URL = '{}?{}'.format(self.GUIDE_URL, urllib.parse.urlencode(_API_ARGS))

        self.TV_OBJECT = xmltv.Tv(
            date=str(date.today()),
            source_info_url=self.GUIDE_URL,
            source_info_name='PlutoTV',
            generator_info_url=self.API_URL,
            generator_info_name='PlutoTV'
        )

        self.CHANNELS = self.XML_PARSER.from_bytes(
            dicttoxml.dicttoxml(
                obj=self.get_json_obj_from_url(json_url=self.GUIDE_URL),
                root=False,
                attr_type=False,
                item_func=lambda x: 'element' if x == '' else x
            ),
            ptvChannels.Root
        )

        self.adapt_ptv_object_to_xmltv_object()
        self.write_to_m3u_file(self.m3u_file_name)

        xmltv_helpers.write_file_from_xml(
            xml_file_path=pathlib.Path(self.xmltv_file_name),
            serialize_clazz=self.TV_OBJECT
        )

    def adapt_ptv_object_to_xmltv_object(self):
        """
        Adapt the PlutoTV data object to XMLTV Object.
        """
        for ptv_chan in self.CHANNELS.element:
            _category = None
            _lang = 'en'
            _rating = None
            _url = None
            if ptv_chan.isStitched:
                _url = [ptv_chan.stitched.urls.urls.url]

            self.TV_OBJECT.channel.append(
                Channel(
                    display_name=[DisplayName(content=[ptv_chan.name], lang=_lang)],
                    icon=[Icon(src=ptv_chan.featuredImage.path)],
                    url=_url,
                    id=ptv_chan.number
                )
            )

            for ptv_prog in ptv_chan.timelines.timelines:
                if ptv_prog.episode.rating is not None:
                    _rating = [xmltv_helpers.get_rating_object(ptv_prog.episode.rating)]
                if ptv_prog.episode.genre is not None or ptv_prog.episode.subGenre is not None:
                    _category = []
                    if ptv_prog.episode.genre is not None:
                        _category.append(Category(content=[ptv_prog.episode.genre], lang=_lang))
                    if ptv_prog.episode.subGenre is not None:
                        _category.append(Category(content=[ptv_prog.episode.subGenre], lang=_lang))
                self.TV_OBJECT.programme.append(
                    Programme(
                        category=_category,
                        channel=ptv_chan.number,
                        clumpidx=None,
                        date=ptv_prog.episode.firstAired,
                        desc=[Desc(content=[ptv_prog.episode.description], lang=_lang)],
                        episode_num=[EpisodeNum(content=[ptv_prog.episode.number], system='onscreen')],
                        icon=[Icon(src=ptv_prog.episode.series.tile.path)],
                        language=Language(content=[_lang], lang=_lang),
                        rating=_rating,
                        start=self.get_proper_date_time(date_time_string=str(ptv_prog.start), new_format=_NEW_DATE_FORMAT_NO_TZ),
                        stop=self.get_proper_date_time(date_time_string=str(ptv_prog.stop), new_format=_NEW_DATE_FORMAT_NO_TZ),
                        sub_title=[SubTitle(content=[ptv_prog.episode.name], lang=_lang)],
                        title=[Title(content=[ptv_prog.title], lang=_lang)],
                        url=_url
                    )
                )

    def write_to_m3u_file(self, m3u_out_file: str):
        """
        Method that writes the loaded channels to an M3U file of your choosing.
        """
        m3u_template = Template("""#EXTM3U
        {%- for channel in channels -%}
        {% if channel.url is not none %}
#EXTINF:-0 channel-id="{{ channel.id }}" tvg-name="{{ channel.display_name[0].content[0] }}" tvg-id"{{ channel.display_name[0].content[0] }}" tvg-logo="{{ channel.icon[0].src }}" group-title="PlutoTV", {{ channel.display_name[0].content[0] }}
{{ channel.url[0] }}
        {% endif %}
        {%- endfor -%}
        """).render(
            channels=self.TV_OBJECT.channel
        )
        self.LOGGER.debug('Writing channels to {}.'.format(m3u_out_file))
        open(m3u_out_file, 'w').write(m3u_template)

    def get_json_obj_from_url(self, json_url: str):
        """
        Get the json object from the specified url.
        :param json_url: The URL the json data is at.
        :return: the json object.
        """
        try:
            self.LOGGER.debug('Attempting to download the json data from the URL {}.'.format(json_url))
            raw_data = urlopen(json_url).read()
            if len(raw_data) == 0:
                self.LOGGER.debug('Couldn\'t scrape data from the url: {}'.format(json_url))
                return None
            else:
                self.LOGGER.debug('Successfully pulled data from the url {} so we will not reconstruct it into a python data object.'.format(json_url))
                return [json.loads(raw_data)]
        except urllib.error.URLError as connectionError:
            self.LOGGER.error('Error getting data from URL {} due to connection issue.'.format(json_url), connectionError)

    def get_proper_date_time(self, date_time_string, new_format):
        """
        Simple Method to help get the current date format and then change
         the format to the desired format.
        :param date_time_string: The string to be re-formatted
        :param new_format: The new format the datetime will return
        :return: The new dateformat
        """
        self.LOGGER.debug('Converting the date_time_string {} to format {}.'.format(date_time_string, new_format))
        if date_time_string != '' and date_time_string is not None:
            if type(date_time_string) is datetime:
                return date_time_string.strftime(new_format)
            else:
                return parser.parse(date_time_string, fuzzy=True).__format__(new_format)


class CustomBoolConverter(Converter):
    """
    Loading the Json into a dict from the pluto tv api converts the value to a python-type True/False
    which is incompatible in JSON format of true/false. (Case). So In this converter I just convert the
    Python data type to lower case.
    """
    def deserialize(self, value: Any, **kwargs: Any) -> bool:
        if isinstance(value, str):
            """This line is the only difference from xsdata packages"""
            val = value.strip().lower()

            if val in ("true", "1"):
                return True

            if val in ("false", "0"):
                return False

            raise ConverterError(f"Invalid bool literal '{value}'")

        return True if value else False

    def serialize(self, value: bool, **kwargs: Any) -> str:
        return "true" if value else "false"


class CustomEnumConverter(Converter):
    """
    Custom enum converter to get rid of un-wanted error messages when deserializing data from xml.
    """
    def deserialize(self, value: Any, data_type: Optional[Type[Enum]] = None, **kwargs: Any) -> Enum or None:
        if data_type is None or not issubclass(data_type, Enum):
            raise ConverterError("Provide a target data type enum class.")

        # Convert string value to the type of the first enum member first, otherwise
        # more complex types like QName, Decimals will fail.
        member: Enum = list(data_type)[0]
        value_type = type(member.value)

        # Suppress warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            real_value = converter.deserialize(value, [value_type], **kwargs)
            """This line is the only difference from xsdata packages"""
            if real_value is None: return None

        # Raise exception if the real value doesn't match the expected type.
        if not isinstance(real_value, value_type):
            raise ConverterError(f"Value must be {value_type} but is {real_value}")

        try:
            # Attempt no1 use the enum constructor
            return data_type(real_value)
        except ValueError:
            pass

        try:
            # Attempt no2 the enum might be derived from
            # xs:NMTOKENS or xs:list removing excess whitespace.
            if isinstance(real_value, str):
                return data_type(" ".join(real_value.split()))

            # Attempt #3 some times enum member init values don't match
            # Try matching canonical repr or member values directly
            repr_value = repr(real_value)
            for x in data_type:
                if repr(x.value) == repr_value or x.value == real_value:
                    return x

            raise ConverterError("Not enum member matched")

        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: Enum, **kwargs: Any) -> str:
        return converter.serialize(value.value, **kwargs)


class CustomStringConverter(Converter):
    """
    This is a custom Proxy Converter to clean data as it's deserialized.
    """
    _EXCLUDED_STRINGS = [
        'Not Rated',
        'No information available',
        'No Rating'
    ]

    def deserialize(self, value: str, **kwargs: Any) -> str or None:
        if isinstance(value, str):
            if value in self._EXCLUDED_STRINGS:
                return None
            return value

    def serialize(self, value: Any, **kwargs: Any) -> str:
        return str(value)


converter.register_converter(bool, CustomBoolConverter())
converter.register_converter(type(Enum), CustomEnumConverter())
converter.register_converter(str, CustomStringConverter())


def main():
    ptv = PlutoTv()
    ptv.main()


if __name__ == "__main__":
    main()
