python-gamesdb
==============

python-gamesdb is a python client for gamesdb api (http://wiki.thegamesdb.net/index.php?title=API_Introduction)

Presently, most but not all API calls are supported.  Retrieval for most images has not yet been developed, however it is
fairly complete for fetching data about games and platforms.

# Prerequisites
The prerequisites for this pacakge are generally provided as a part of base Python and should not require any special installation.

* [urllib](http://docs.python.org/2/library/urllib.html): Installed by default with most modern Python interpreters.  Used to make HTTP requests and read responses.
* [urllib2](http://docs.python.org/2/library/urllib2.html): Installed by default with most modern Python interpreters.  Used to make HTTP requests and read responses
* [ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html): Installed by default with most modern Python interpreters.  Used to parse XML responses.

#Usage

## Basics

In order to use this library you must first instantiate a GamesDB object.

```python
from gamesdb.api import API
gamesdb_api = API()
```

## Specific Calls

### Get Platforms List

[GamesDB GetPlatformsList API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatformsList)

This call takes no arguments, and returns a list of Platform objects, with the id, name, and alias fields supplied:

```python
platform_list = gamesdb_api.get_platforms_list()
for platform in platform_list:
    print platform.id, "-", platform.name, "-", platform.alias
```

**Output:**

```
5 - 3DO - 3do
4911 - Amiga - amiga
4914 - Amstrad CPC - amstrad-cpc
4916 - Android - amstrad-cpc
23 - Arcade - arcade
22 - Atari 2600 - atari-2600
...
```


### Get Platform

[GamesDB GetPlatform API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatform)

This call retrieves all available details for a platform, based off of the id returned in get_platforms_list().

```python
atari_platform = gamesdb_api.get_platform('22')
print atari_platform.name
print atari_platform.overview
```

**Output:**

```
Atari 2600
The Atari 2600 is a video game console released in October 1977 by Atari, Inc. It is credited with popularizing the use of microprocessor-based hardware and cartridges containing game code, instead of having non-microprocessor dedicated hardware with all games built in. The first game console to use this format was the Fairchild Channel F; however, the Atari 2600 receives credit for making the plug-in concept popular among the game-playing public.
The console was originally sold as the Atari VCS, for Video Computer System. Following the release of the Atari 5200, in 1982, the VCS was renamed &quot;Atari 2600&quot;, after the unit&#039;s Atari part number, CX2600. The 2600 was typically bundled with two joystick controllers, a conjoined pair of paddle controllers, and a cartridge game—initially Combat and later Pac-Man.

The Atari 2600 was wildly successful, and during much of the 1980s, &quot;Atari&quot; was a synonym for this model in mainstream media and, by extension, for video games in general.
```

### Get Platform Games

[GamesDB GetPlatformGames API Call](http://wiki.thegamesdb.net/index.php?title=GetPlatformGames)

Retrieve a list of games based on the platform id retrieved in get_platform_list, with id, title, and (if available) release date populated.  Note that at the moment, release date comes back inconsistently formatted based on what the API response supplies.

```python
atari_games_list = gamesdb_api.get_platform_games('22') # Atari 2600 Platform id
for game in atari_games_list:
    print game.id, "-", game.title, "-", game.release_date
```

**Output:**

```
206 - Commando - None
207 - Dig Dug - 01/01/1982
10128 - H.E.R.O. - 01/01/1984
1292 - Ghostbusters - 1984
1341 - Amidar - 01/01/1982
1342 - Asteroids - 08/01/1979
1343 - Battlezone - 01/01/1983
1344 - Blackjack - 01/01/1977
1345 - Casino - None
1346 - Centipede - 01/01/1982
1347 - Defender - 01/01/1980
1348 - Gravitar - None
1349 - Indy 500 - 01/01/1977
1350 - Joust - None
...
```
### Get Game

[GamesDB GetGame API Call](http://wiki.thegamesdb.net/index.php?title=GetGame)

Retrieve all of the available details for a game or list of games, based off of the game id or name.  If passing in name, you may optionally filter results by Platform.  Note that when your query returns only one game (as it the case when querying by id) it will return one game.  When your query returns more than one item, it will return a list of Games.  When your query returns no results, None will be returned.

Note that GetGame will tree name arguments with spaces as an OR search operation.  For example searching where name="mega man" will return all games containing either "mega" or "man" in their title.  This is different that GetGamesList, which would treat the same search as an AND operation.

#### Get Game by id

```python
game = gamesdb_api.get_game(id="1350")
print game.title
print game.overview
print game.genres
print game.developer
```

**Output:**

```
Joust
Joust is a platforming game where the player controls a yellow knight riding a flying ostrich from a third-person perspective. The player navigates the protagonist around the game world, which consists of rock platforms floating above a flat island surrounded by lava.
Platform
Williams Electronics
```
#### Get Game by Name

```python
mega_man_games = gamesdb_api.get_game(name="mega man")
for game in mega_man_games:
    print game.title
    print game.platform
    print "---------------------"
```

**Output:**

```
Mega Man
Nintendo Entertainment System (NES)
---------------------
Mega Man Zero
Nintendo Game Boy Advance
---------------------
Mega Man Soccer
Super Nintendo (SNES)
---------------------
Mega Man 3
Nintendo Game Boy
---------------------
Mega Man Xtreme
Nintendo Game Boy Color
---------------------
Mega Man X5
Sony Playstation
---------------------

...

Mega Bomberman
Sega Mega Drive
---------------------
Mega Turrican
Sega Genesis
---------------------
Mega Force
Atari 2600
---------------------
Mega Bomberman
Sega Genesis
---------------------
Low G Man: The Low Gravity Man
Nintendo Entertainment System (NES)
---------------------
Mega-Lo-Mania
Super Nintendo (SNES)
---------------------
WarioWare, Inc.: Mega Microgames!
Nintendo Game Boy Advance
---------------------
Sonic Mega Collection
Nintendo GameCube
---------------------
WarioWare, Inc.: Mega Party Games!
Nintendo GameCube
---------------------
Eight Man
NeoGeo
 
```
#### Get Game by Name and Platform

```python
mega_man_games = gamesdb_api.get_game(name="mega man", platform='Nintendo Entertainment System (NES)')
for game in mega_man_games:
    print game.title
    print game.platform
    print "---------------------"
```

**Output:**

```
Mega Man
Nintendo Entertainment System (NES)
---------------------
Mega Man 2
Nintendo Entertainment System (NES)
---------------------
Mega Man 5
Nintendo Entertainment System (NES)
---------------------
Mega Man 3
Nintendo Entertainment System (NES)
---------------------
Mega Man 4
Nintendo Entertainment System (NES)
---------------------
Mega Man 6
Nintendo Entertainment System (NES)
---------------------
Low G Man: The Low Gravity Man
Nintendo Entertainment System (NES)
---------------------
Pac-Man
Nintendo Entertainment System (NES)
---------------------
Ms. Pac-Man
Nintendo Entertainment System (NES)
---------------------
Spider-Man: Return of the Sinister Six
Nintendo Entertainment System (NES)
---------------------
Metal Mech: Man & Machine
Nintendo Entertainment System (NES)
---------------------
The Simpsons: Bartman Meets Radioactive Man
Nintendo Entertainment System (NES)
... 
```

### Get Games List

[GamesDB GetGamesList API Call](http://wiki.thegamesdb.net/index.php?title=GetGamesList)

Retrieve the id, title, release date (when available) and platform for a list of games, based off of the name, and optionally the platform and genre.  This call will always return a list of Games.

Note that GetGamesList will treat name arguments with spaces as an AND search operation.  For example searching where name="mega man" will return all games containing both "mega" and "man" in their title.  This is different that GetGame, which would treat the same search as an OR operation.

#### Get Games List by Name

```python
mega_man_games = gamesdb_api.get_games_list(name="mega man")
for game in mega_man_games:
    print game.title
    print game.platform
    print game.release_date
    print "---------------------"
```

**Output:**

```
Mega Man
Nintendo Entertainment System (NES)
12/17/1987
---------------------
Mega Man Zero
Nintendo Game Boy Advance
04/26/2002
---------------------
Mega Man 5
Nintendo Entertainment System (NES)
12/04/1992
---------------------
Mega Man X
Super Nintendo (SNES)
01/01/1994
---------------------
Mega Man 7
Super Nintendo (SNES)
03/24/1995
---------------------
Mega Man 2
Nintendo Entertainment System (NES)
11/24/1988
---------------------
Mega Man 3
Nintendo Entertainment System (NES)
09/28/1990
---------------------
Mega Man 4
Nintendo Entertainment System (NES)
12/06/1991
---------------------
Mega Man 6
Nintendo Entertainment System (NES)
10/06/1992
---------------------
Mega Man 8
Sony Playstation
12/17/1996
---------------------
Mega Man Legends
Sony Playstation
08/31/1998
---------------------
Mega Man X4
Sony Playstation
08/10/1997
---------------------
Mega Man X2
Super Nintendo (SNES)
01/01/1995
---------------------
Mega Man X3
Super Nintendo (SNES)
01/01/1996
---------------------
Mega Man 64
Nintendo 64
11/22/2000
---------------------
Mega Man & Bass
Nintendo Game Boy Advance
08/10/2002
---------------------
Mega Man Zero 2
Nintendo Game Boy Advance
05/02/2003
---------------------
Mega Man Zero 3
Nintendo Game Boy Advance
04/23/2004
---------------------
Mega Man Zero 4
Nintendo Game Boy Advance
04/21/2005
---------------------
Mega Man X6
Sony Playstation
12/04/2001
---------------------
```

#### Get Games List by Name and PLatform

```python
mega_man_games = gamesdb_api.get_games_list(name="mega man", platform='Sony Playstation')
for game in mega_man_games:
    print game.title
    print game.platform
    print game.release_date
    print "---------------------"
```

**Output:**

```
Mega Man 8
Sony Playstation
12/17/1996
---------------------
Mega Man Legends
Sony Playstation
08/31/1998
---------------------
Mega Man X4
Sony Playstation
08/10/1997
---------------------
Mega Man X6
Sony Playstation
12/04/2001
---------------------
Mega Man X5
Sony Playstation
01/31/2001
---------------------
Mega Man X3
Sony Playstation
04/26/1996
---------------------
Mega Man Battle & Chase
Sony Playstation
11/30/1998
---------------------
Mega Man Legends 2
Sony Playstation
10/24/2000
---------------------
Spider-Man
Sony Playstation
01/01/2001
---------------------
Shadow Man
Sony Playstation
09/30/1999
---------------------
Pac-Man World
Sony Playstation
01/01/2000
---------------------
Action Man: Operation Extreme
Sony Playstation
11/08/2000
---------------------
Pac-Man World 20th Aniversary
Sony Playstation
09/30/1999
---------------------
Ms. Pac-Man Maze Madness
Sony Playstation
09/08/2000
---------------------
Spider-Man 2: Enter Electro
Sony Playstation
08/16/2001
---------------------
Iron Man / X-O Manowar in Heavy Metal
Sony Playstation
10/31/1996
---------------------
```

#### Get Games List by Name and Genre
Note that you can pass in genre and platform independently, name is the only required field.

```python
mega_man_games = gamesdb_api.get_games_list(name="mega man", platform='Sony Playstation', genre='platform')
for game in mega_man_games:
    print game.title
    print game.platform
    print game.release_date
    print "---------------------"
```

**Output:**

```
Mega Man X6
Sony Playstation
12/04/2001
---------------------
Mega Man Legends 2
Sony Playstation
10/24/2000
---------------------
Pac-Man World 20th Aniversary
Sony Playstation
09/30/1999
---------------------
```



h2. Classes

At present, there are two main class types uses to present results.  The specific entries that are populated will vary based off othe query and the actualy data available for your object(s).

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
