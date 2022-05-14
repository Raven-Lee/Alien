import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """a class that show score info"""

    def  __init__(self, ai_settings, screen, stats) -> None:
        """init attribute relate to score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font setting for showing score
        self.text_color = (51, 51, 51)
        self.font = pygame.font.SysFont(None, 48)

        # prepare score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """render score to image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: "+"{:,}".format(rounded_score) 
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # put score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        """show score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # draw left ships
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """render highest score"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str ="Best Record: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # put highest score at the middle top 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_level(self):
        """render level into image"""
        self.level_image = self.font.render("Level: "+str(self.stats.level),True, self.text_color, self.ai_settings.bg_color)

        # put level image under score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """render ship left into image"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    