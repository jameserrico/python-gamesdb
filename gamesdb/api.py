import urllib2
import xml.etree.ElementTree as ET

class GamesList(object):

    def __init__(self, id, title, release_date, platform=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.platform = platform

class PlatformList(object):

    def __init__(self, id, name, alias):
        self.id = id
        self.name = name
        self.alias = alias

class Platform(object):

    def __init__(self, id, name, console=None, controller=None, graphics=None, max_controllers=None,rating=None,
                 display=None, manufacturer=None, cpu=None, memory=None, sound=None, media=None, developer=None,
                 overview=None):
        self.id = id
        self.name = name
        self.console = console
        self.controller = controller
        self.overview = overview
        self.developer = developer
        self.manufacturer = manufacturer
        self.cpu = cpu
        self.memory = memory
        self.graphics = graphics
        self.sound = sound
        self.display = display
        self.media = media
        self.max_controllers = max_controllers
        self.rating = rating

class APIException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class API(object):

    @staticmethod
    def make_call(api_url):
        # api_url is expected to be the fully constructed URL, with any needed arguments appended.
        # This function will simply make the call, and return the response as an ElementTree object for parsing,
        # If response cannot be parsed because it is not valid XML, this function assumes an API error and raises an
        # APIException, passing forward the pages contents (which generally gives some indication of the error.
        page = urllib2.urlopen(api_url).read()
        # Make sure the XML Parser doesn't return a ParsError.  If it does, it's probably and API Issue, so raise an
        # exception, printing the response from the API call.
        try:
            xml_response = ET.fromstring(page)
        except ET.ParseError:
            raise APIException(page)
        return  xml_response

    def get_platforms_list(self):
        platforms_list = []
        GET_PLATFORMS_LIST_ENDPOINT = 'http://thegamesdb.net/api/GetPlatformsList.php'
        xml_response = self.make_call(GET_PLATFORMS_LIST_ENDPOINT)
        for element in xml_response.iter(tag="Platform"):
            for subelement in element:
                if subelement.tag == 'id':
                    platform_id = subelement.text
                if subelement.tag == 'name':
                    platform_name = subelement.text
                if subelement.tag == 'alias':
                    platform_alias = subelement.text
            platforms_list.append(PlatformList(platform_id, platform_name, platform_alias))

        return platforms_list

    def get_platform(self, id):
        # TODO Add support for fetching platform images under the <Images> element
        GET_PLATFORM_ENDPOINT = 'http://thegamesdb.net/api/GetPlatform.php?id='
        xml_response = self.make_call(GET_PLATFORM_ENDPOINT + str(id))
        # TODO These are all optional fields.  There's probably a better way to handle this than initing them to None.
        platform_id = None
        platform_name = None
        platform_console = None
        platform_controller = None
        platform_graphics = None
        platform_max_controllers = None
        platform_rating = None
        platform_display = None
        platform_manufacturer = None
        platform_cpu = None
        platform_memory = None
        platform_sound = None
        platform_media = None
        platform_developer = None
        platform_overview = None
        for element in xml_response.iter(tag="Platform"):
            for subelement in element:
                if subelement.tag == 'id':
                    platform_id = subelement.text
                if subelement.tag == 'Platform':
                    platform_name = subelement.text
                if subelement.tag == 'console':
                    platform_console = subelement.text
                if subelement.tag == 'controller':
                    platform_controller = subelement.text
                if subelement.tag == 'overview':
                    platform_overview = subelement.text
                if subelement.tag == 'developer':
                    platform_developer = subelement.text
                if subelement.tag == 'manufacturer':
                    platform_manufacturer = subelement.text
                if subelement.tag == 'cpu':
                    platform_cpu = subelement.text
                if subelement.tag == 'memory':
                    platform_memory = subelement.text
                if subelement.tag == 'graphics':
                    platform_graphics = subelement.text
                if subelement.tag == 'sound':
                    platform_sound = subelement.text
                if subelement.tag == 'display':
                    platform_display = subelement.text
                if subelement.tag == 'media':
                    platform_media = subelement.text
                if subelement.tag == 'max_controllers':
                    platform_max_controllers = subelement.text
                if subelement.tag == 'rating':
                    platform_rating = subelement.text
        if (platform_id == None or platform_name == None):
            raise APIException("get_platform returned a result without required fields id or platform")
        return Platform(platform_id, platform_name, platform_console, platform_controller, platform_graphics,
                        platform_max_controllers, platform_rating, platform_display, platform_manufacturer,
                        platform_cpu, platform_memory, platform_sound, platform_media, platform_developer,
                        platform_overview)

    def get_platform_games(self, platform_id=None):
        platform_games_list = []
        GET_PLATFORM_GAMES_LIST_ENDPOINT = 'http://thegamesdb.net/api/GetPlatformGames.php?platform='
        xml_response = self.make_call(GET_PLATFORM_GAMES_LIST_ENDPOINT + str(platform_id))
        for element in xml_response.iter(tag="Games"):
            for subelement in element:
                if subelement.tag == 'id':
                    platform_games_list_id = subelement.text
                if subelement.tag == 'GameTitle':
                    platform_games_list_name = subelement.text
                if subelement.tag == 'ReleaseDate':
                    platform_games_list_release_date = subelement.text
            platform_games_list.append(GamesList(platform_games_list_id, platform_games_list_name, platform_games_list_release_date))
        return platform_games_list





