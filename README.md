python-gamesdb
==============

python-gamesdb is a python client for gamesdb api (http://wiki.thegamesdb.net/index.php?title=API_Introduction)

Presently, most but not all API calls are supported.  Retrieval for most images has not yet been developed, however it is
fairly complete for fetching data about games and platforms.

# Prerequisites
* [urllib](http://docs.python.org/2/library/urllib.html): Installed by default with most modern Python interpreters.  Used to make HTTP requests and read responses.
* [urllib2](http://docs.python.org/2/library/urllib2.html): Installed by default with most modern Python interpreters.  Used to make HTTP requests and read responses
* [ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html): Installed by default with most modern Python interpreters.  Use to parse XML responses.

#Usage

## Basics

In order to m

## Specific Calls

#### Get Platforms List

[GamesDB GetPlatformsList API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatformsList)

#### Get Platform

[GamesDB GetPlatform API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatform)

#### Get Platform Games

[GamesDB GetPlatformGames API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatformGames)

#### Get Game

[GamesDB GetGame API Call](http://wiki.thegamesdb.net/index.php?title=GetGame)

#### Get Games List

[GamesDB GetGamesList API Call](http://wiki.thegamesdb.net/index.php?title=GetGamesList)

h2. Classes

At present, there are two main class types uses to present results:

* Game
  * id
  * title
  * release_date
  * platform
  * overview
  * esrb_rating
  * genres
  * players
  * coop
  * youtube_url
  * publisher
  * developer
  * rating
  * logo_url
* Platform
  * id
  * name
  * alias
  * console
  * controller
  * overview
  * developer
  * manufacturer
  * cpu
  * memory
  * graphics
  * sound
  * display
  * media
  * max_controllers
  * rating
