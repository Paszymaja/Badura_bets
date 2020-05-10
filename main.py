import os
from riotwatcher import LolWatcher

region = 'EUN1'
watcher = LolWatcher(os.getenv('LOL_KEY'))
badura = watcher.summoner.by_name(region, 'Ahegao Loli')
badura_accountId = badura['id']
live_game = watcher.spectator.by_summoner(region, badura_accountId)
if live_game['gameLength'] > 90 and live_game['mapId'] == 1:
    print('bets are open: ')

print(live_game)

