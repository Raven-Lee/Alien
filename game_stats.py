class GameStats():
    """track stats of game"""
    def __init__(self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        
    
    def reset_stats(self):
        """initialize stat that may change during runing"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1