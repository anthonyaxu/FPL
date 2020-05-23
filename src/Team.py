
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

    # def team_players(self, )