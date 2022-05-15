from turtle import screensize
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """init ship for its location and other setting"""
    
    def __init__(self, ai_setting, screen):
        """init ship for its location and other setting"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        #load image
        image = pygame.image.load('img/ship.bmp')
        self.image = image 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # moving flag 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # put ship at the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float number for center attribute
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom) 
    def blitme(self):
        """draw ship at certain location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """move when change moving flg and ship not touching the edge of the screen"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def center_ship(self):
        """put ship in the center"""
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom