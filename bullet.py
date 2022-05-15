from curses.ascii import SP
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """init a bullet at which ship located"""
        super(Bullet, self).__init__()
        self.screen = screen

        # init a rect for bullet at (0,0), then move to the right place
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store location with float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed
        
    def update(self):
        """bullet fly toward up"""
        # update bullet location in float
        self.y -= self.speed_factor
        # update bullet location 
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the scree"""
        pygame.draw.rect(self.screen, self.color, self.rect)