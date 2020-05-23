import requests
from src import Player, Team
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

    def get_team(self, team_id):
        for team in self.teams:
            if type(team_id) is int and team_id == team['id']:
                return Team.Team(team)
            if type(team_id) is str and lowercase(team_id) == lowercase(team['name']):
                return Team.Team(team)

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
    t = fpl.get_team('aston villa')
    print(t.short_name)
