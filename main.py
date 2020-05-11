import os
import time
from riotwatcher import LolWatcher, ApiError

region = 'EUN1'
watcher = LolWatcher(os.getenv('LOL_KEY'))
badura = watcher.summoner.by_name(region, 'Ahegao Loli')
badura_accountId = badura['id']
wait_for_finish = False

timeout = time.time() + 90
bets = []
game_Id = 0

if not wait_for_finish:
    while True:
        time.sleep(5)
        try:
            live_game = watcher.spectator.by_summoner(region, badura_accountId)
            print('game found')
            millis = int(round(time.time() * 1000))
            print(live_game)
            game_Id = live_game['gameId']
            if live_game['mapId'] == 11 and live_game['gameStartTime'] - millis < 78000:
                print('bets open')
                while time.time() < timeout:
                    bets.append(int((input('Podaj czas w sec '))))
                print('bets close')
                wait_for_finish = True
            break

        except ApiError as err:
            if err.response.status_code == 404:
                print('game not found')
            else:
                raise
else:
    try:
        game_data = watcher.match.by_id(region, game_Id)

    except ApiError as err:
        if err.response.status_code == 404:
            print('game not finnished')
