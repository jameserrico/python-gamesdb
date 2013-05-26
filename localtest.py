from gamesdb.api import API

gamesdb_api = API()
# atari_games_list = gamesdb_api.get_platform_games('22')
# for game in atari_games_list:
#     print game.id, "-", game.title, "-"
atari_joust = gamesdb_api.get_game(id="1350")
print atari_joust.title, atari_joust.overview, atari_joust.genres, atari_joust.logo_url. atari_joust.developer

# print game.title, game.overview, game.genres, game.logo_url. game.developer
# for platform in platform_list:
#     print platform.id, "-", platform.name, "-", platform.alias
#     this_platform = gamesdb_api.get_platform(platform.id)
#     # platforms.append(this_platform)
#     print this_platform.name, '-', this_platform.id
#     this_platform_games = gamesdb_api.get_platform_games(platform.id)
#     for platform_game in this_platform_games:
#         game_results = gamesdb_api.get_game(id=platform_game.id)
#         for game in game_results:
#             print game.id, "-", game.title, " ", game.overview
#             break
#         break
#     break
# mega_man_games = gamesdb_api.get_games_list("Mega Man")
# for game in mega_man_games:
#     print game.id, "-", game.title, " ", game.platform
#
