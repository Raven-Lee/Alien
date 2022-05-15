class Settings():
    """all settings for Alien Invasion"""

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship
        self.ship_speed_factor = 1
        self.ship_limit = 3
        # bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        self.bullet_penatration = True
        # alien 
        self.alien_speed = 0.15
        self.fleet_drop_speed = 30
        # alien_attack
        self.alien_attack_frequncy = 2
        self.alien_attack_posibility = 90
        self.alien_attack_speed = 0.5
        self.alien_attack_width = 3
        self.alien_attack_height =15
        self.alien_attack_color = (255, 64, 64)
        self.alien_attack_allowed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # gameing pace
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
                

    def initialize_dynamic_settings(self):
        """initialize dynamic setting"""
        # speed
        self.ship_speed_factor =  1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # point
        self.alien_points = 10

        # fleet moving toward right when equal to 1, toward left when euqal to -1
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed setting"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points += 5