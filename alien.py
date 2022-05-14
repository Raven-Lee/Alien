import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # load image, set rect attribute
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        # init alien location at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store exact location for alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move to right or left"""
        self.x += self.ai_setting.alien_speed * self.ai_setting.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    