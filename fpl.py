import requests
from src import Player
from utils import *

BASE_URL = 'https://fantasy.premierleague.com/api/'

API_URLS = {
    'static': '{}bootstrap-static/'.format(BASE_URL),
    'fixtures': '{}fixtures'.format(BASE_URL),
    'player': '{}element-summary/{{}}'.format(BASE_URL)
}

"""
FPL attributes: events, game_settings, phases, teams, total_players, 
                  elements, element_stats, element_types
"""

class FPL:
    def __init__(self):
        static = requests.get(API_URLS['static']).json()
        for attr, value in static.items():
            setattr(self, attr, value)

    def get_player(self, player_id):
        for player in self.elements:
            if type(player_id) is int and player_id == player['id']:
                return Player.Player(player)
            if type(player_id) is str:
                player_name = deaccent(player['web_name'])
                if lowercase(player_id) == lowercase(player_name):
                    return Player.Player(player)

    # @property
    # def events(self):
    #     return self._events

    # @property
    # def phases(self):
    #     return self._phases

    # @property
    # def teams(self):
    #     return self._teams
    
    # @property
    # def elements(self):
    #     return self._elements


if __name__ == '__main__':
    fpl = FPL()
    p = fpl.get_player('ozil')
    print(p.web_name)
