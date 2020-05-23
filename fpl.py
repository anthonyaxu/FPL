import requests

BASE_URL = 'https://fantasy.premierleague.com/api/'

API_URLS = {
    'static': '{}bootstrap-static/'.format(BASE_URL),
    'fixtures': '{}fixtures'.format(BASE_URL),
    'player': '{}element-summary/{{}}'.format(BASE_URL)
}

class FPL:
    def __init__(self):
        data = self.fpl_request()

        self._events = data['events']
        self._game_settings = data['game_settings']
        self._phases = data['phases']
        self._teams = self.format_data(data['teams'])
        self._players = self.format_data(data['elements'])
        self._player_stats = self.format_data(data['element_stats'])
        self._positions = self.format_data(data['element_types'])

    def fpl_request(self):
        return requests.get(API_URLS['static']).json()
 
    def format_data(self, data):
        return data

    def get_events(self):
        return self._events

    def get_game_settings(self):
        return self._game_settings

    def get_phases(self):
        return self._phases

    def get_teams(self):
        return self._teams

    def get_players(self):
        return self._players

    def get_player_stats(self):
        return self._player_stats

    def get_positions(self):
        return self._positions


if __name__ == '__main__':
    fpl = FPL()
