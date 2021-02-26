from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.exceptions import ConverterError
from xsdata.formats.converter import Converter, converter
from xsdata.models.datatype import XmlDate, XmlDateTime
from xsdata.models.xsd import Any


@dataclass
class Avod:
    class Meta:
        name = "AVOD"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Id:
    class Meta:
        name = "_id"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Category:
    class Meta:
        name = "category"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ChatEnabled:
    class Meta:
        name = "chatEnabled"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ChatRoomId:
    class Meta:
        name = "chatRoomId"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Clip:
    class Meta:
        name = "clip"

    originalReleaseDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CohortMask:
    class Meta:
        name = "cohortMask"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ColorLogoPng:
    class Meta:
        name = "colorLogoPNG"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ColorLogoSvg:
    class Meta:
        name = "colorLogoSVG"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Description:
    class Meta:
        name = "description"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DirectOnly:
    class Meta:
        name = "directOnly"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DisplayName:
    class Meta:
        name = "displayName"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DistributeAs:
    class Meta:
        name = "distributeAs"

    avod: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AVOD",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Duration:
    class Meta:
        name = "duration"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Favorite:
    class Meta:
        name = "favorite"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Featured:
    class Meta:
        name = "featured"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FeaturedImage:
    class Meta:
        name = "featuredImage"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FeaturedOrder:
    class Meta:
        name = "featuredOrder"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FirstAired:
    class Meta:
        name = "firstAired"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Genre:
    class Meta:
        name = "genre"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Hash:
    class Meta:
        name = "hash"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IsStitched:
    class Meta:
        name = "isStitched"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LiveBroadcast:
    class Meta:
        name = "liveBroadcast"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Logo:
    class Meta:
        name = "logo"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Name:
    class Meta:
        name = "name"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Number:
    class Meta:
        name = "number"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OnDemand:
    class Meta:
        name = "onDemand"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OnDemandDescription:
    class Meta:
        name = "onDemandDescription"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OriginalContentDuration:
    class Meta:
        name = "originalContentDuration"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OriginalReleaseDate:
    class Meta:
        name = "originalReleaseDate"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Path:
    class Meta:
        name = "path"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PlutoOfficeOnly:
    class Meta:
        name = "plutoOfficeOnly"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Poster:
    class Meta:
        name = "poster"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Rating:
    class Meta:
        name = "rating"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SessionUrl:
    class Meta:
        name = "sessionURL"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Slug:
    class Meta:
        name = "slug"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SolidLogoPng:
    class Meta:
        name = "solidLogoPNG"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SolidLogoSvg:
    class Meta:
        name = "solidLogoSVG"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Start:
    class Meta:
        name = "start"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Stop:
    class Meta:
        name = "stop"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SubGenre:
    class Meta:
        name = "subGenre"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Summary:
    class Meta:
        name = "summary"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Thumbnail:
    class Meta:
        name = "thumbnail"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Tile:
    class Meta:
        name = "tile"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Title:
    class Meta:
        name = "title"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Tmsid:
    class Meta:
        name = "tmsid"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Type:
    class Meta:
        name = "type"

    value: Optional["Type.Value"] = field(
        default=None,
    )

    class Value(Enum):
        FILM = "film"
        HLS = "hls"
        LIVE = "live"
        MUSICVIDEO = "music-video"
        NOINFORMATIONAVAILABLE = "No information available"
        TV = "tv"
        WEBORIGINAL = "web-original"


@dataclass
class Url:
    class Meta:
        name = "url"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Urls:
    class Meta:
        name = "urls"

    type: Optional["Urls.Value"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    urls: Optional["Urls"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    class Value(Enum):
        FILM = "film"
        HLS = "hls"
        LIVE = "live"
        MUSICVIDEO = "music-video"
        NOINFORMATIONAVAILABLE = "No information available"
        TV = "tv"
        WEBORIGINAL = "web-original"


@dataclass
class Visibility:
    class Meta:
        name = "visibility"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Series:
    class Meta:
        name = "series"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    displayName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    featuredImage: Optional[FeaturedImage] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    slug: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tile: Optional[Tile] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type: Optional["Series.Value"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
            "required": True,
        }
    )

    class Value(Enum):
        FILM = "film"
        HLS = "hls"
        LIVE = "live"
        MUSICVIDEO = "music-video"
        NOINFORMATIONAVAILABLE = "No information available"
        TV = "tv"
        WEBORIGINAL = "web-original"


@dataclass
class Stitched:
    class Meta:
        name = "stitched"

    urls: Optional[Urls] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sessionUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionURL",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Episode:
    class Meta:
        name = "episode"

    clip: Optional[Clip] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    distributeAs: Optional[DistributeAs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    featuredImage: Optional[FeaturedImage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    firstAired: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    liveBroadcast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    originalContentDuration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    poster: Optional[Poster] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    series: Optional[Series] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    slug: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    subGenre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    thumbnail: Optional[Thumbnail] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Timelines:
    class Meta:
        name = "timelines"

    episode: Optional[Episode] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    timelines: List["Timelines"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
        }
    )


@dataclass
class Element:
    class Meta:
        name = "element"

    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    chatEnabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    chatRoomId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cohortMask: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    colorLogoSvg: Optional[ColorLogoSvg] = field(
        default=None,
        metadata={
            "name": "colorLogoSVG",
            "type": "Element",
        }
    )
    colorLogoPng: Optional[ColorLogoPng] = field(
        default=None,
        metadata={
            "name": "colorLogoPNG",
            "type": "Element",
        }
    )
    directOnly: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    element: List["Element"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    favorite: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    featured: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    featuredOrder: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    featuredImage: Optional[FeaturedImage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    isStitched: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    onDemand: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    onDemandDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    plutoOfficeOnly: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    slug: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    solidLogoPng: Optional[SolidLogoPng] = field(
        default=None,
        metadata={
            "name": "solidLogoPNG",
            "type": "Element",
        }
    )
    solidLogoSvg: Optional[SolidLogoSvg] = field(
        default=None,
        metadata={
            "name": "solidLogoSVG",
            "type": "Element",
        }
    )
    stitched: Optional[Stitched] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    thumbnail: Optional[Thumbnail] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tile: Optional[Tile] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    logo: Optional[Logo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    timelines: Optional[Timelines] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tmsid: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    visibility: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    element: List[Element] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )