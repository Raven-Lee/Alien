import shelve
from os.path import exists

class GameStats():
    """track stats of game"""
    def __init__(self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.get_hight_score()
        
    
    def reset_stats(self):
        """initialize stat that may change during runing"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_hight_score(self):
        """get hight score from file"""
        score_file = 'data/score.txt'
        with shelve.open(score_file) as d:
            return d['score']
        