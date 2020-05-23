
"""
Player attributes: element_type, ep_next, ep_this, event_points, first_name, second_name,
                   web_name, form, id, now_cost, points_per_game, selected_by_percent,
                   team, team_code, total_points, value_form, value_season, minutes, 
                   goals_scored, assists, clean_sheets, goals_conceeded, own_goals, 
                   penalties_saved, penalties_missed, yellow_cards, red_cards, saves, bonus,
                   bps, influence, creativity, threat

"""

class Player:
    def __init__(self, information):
        for attribute, value in information.items():
            setattr(self, attribute, value)

    # Points per 90 min
    def pp90(self):
        return round((self.total_points/self.minutes)*90, 1)

    # Points per cost
    def ppcost(self):
        return round(self.total_points/(self.now_cost*0.1), 1)