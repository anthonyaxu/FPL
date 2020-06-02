import requests
from fpl import BASE_URL, API_URLS
from . import Player

"""
Team attributes: code, win, draw, lose, form, id, name, short_name, player, points,
                 position, strength, strength_overall_home, strength_overall_away,
                 strength_attack_home, strength_attack_away, strength_defence_home
                 strength_defence_away
"""

class Team:
    def __init__(self, information):
        for attribute, value in information.items():
            setattr(self, attribute, value)

    # Return all players in each team
    def get_players(self, players = []):
        elements = requests.get(API_URLS['static']).json()['elements']
        for player in elements:
            if player['team'] == self.id:
                players.append(Player.Player(player))
        return players

    # Sum of FPL points for every player in the team
    def total_points(self):
        total_points = 0
        players = self.get_players()
        for player in players:
            total_points += player.total_points
        return total_points