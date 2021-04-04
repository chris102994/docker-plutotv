## [chris102994/docker-plutotv](https://github.com/chris102994/docker-plutotv)

[![https://www.pluto.tv/](https://pluto.tv/assets/images/og-logo-v5.png)](https://www.pluto.tv/)

[![Build Status](https://travis-ci.com/chris102994/docker-plutotv.svg?branch=master)](https://travis-ci.com/chris102994/docker-plutotv)
[![Microbadger Size & Layers](https://images.microbadger.com/badges/image/christopher102994/docker-plutotv.svg)](https://microbadger.com/images/christopher102994/docker-plutotv)
[![Image Pulls](https://img.shields.io/docker/pulls/christopher102994/docker-plutotv)](https://hub.docker.com/repository/docker/christopher102994/docker-plutotv)
[![Alpine](https://images.microbadger.com/badges/version/christopher102994/docker-plutotv:ubuntu-18-latest.svg)](https://microbadger.com/images/christopher102994/docker-plutotv:ubuntu-18-latest)


[PlutoTV](https://www.PlutoTV.com/) s an American internet television service owned by ViacomCBS. Pluto is a free, advertiser-supported video on demand (AVOD) service that primarily offers a selection of programming content through digital linear channels designed to emulate the experience of traditional broadcast programming. The service's revenue is generated from video advertisements seen during programming within ad breaks structured similarly to those found on conventional television.

Pluto TV licenses its content directly from providers, and as of March 2020 has deals with 170 content partners providing more than 250 channels and 100,000 unique hours worth of programming. Its content is available via its website and supported apps.

This is a simple project that scrapes the website and generates an M3U playlist every 8 hours along with a XMLTV object that is hosted over NGINX.

The XMLTV and M3U playlist can be directly imported to Emby or Plex. Or if you'd like a buffer you can also import them into xteve or tvheadend. 


## Docker
```
docker run \
	--name=docker-plutotv \
	-p 8000:8000 \
	-v </path/to/appdata/config>:/config \
	--restart unless-stopped \
	christopher102994/docker-plutotv:ubuntu-18-latest
```

## Parameters
Container specific parameters passed at runtime. The format is `<external>:<internal>` (e.g. `-p 443:22` maps the container's port 22 to the host's port 443).

| Parameter | Function |
| -------- | -------- |
| -p 8000 | This is the port inside the container by default however, you can map the outside port to be the same as the inner port. (Default 8000)  |
| -v /config | The directory where the application will store configuration information. |
| -e USERNAME | The Username you wish to run as. (Optional) |
| -e GROUPNAME | The Groupname you wish to run as. (Optional) |
| -e PUID | The UID you wish to run and save files as. (Optional) |
| -e PGID | The GID you wish to run and save files as. (Optional) |
| -e LOG_LEVEL | The Python Logging log level for the PTV Scraper. (Default: ERROR) |
| -e PLUTO_USER_ID | Your Pluto User ID. (Default: None) |
## Application Setup

The basic index is available at `http://<ip>:<port>/`

This will build and allow you to point your M3U Tuner to `http://<ip>:<port>/PlutoTV.m3u`
and your XEPG tuner to `http://<ip>:port/PlutoTVGuide.xml`
