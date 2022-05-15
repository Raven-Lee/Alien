import pygame
from pygame.sprite import Sprite

class Alien_Bullet(Sprite):

    def __init__(self, ai_settings, screen, alien) -> None:
        super().__init__()
        self.screen = screen

        # init a rect for the attack at (0, 0), then move to the right place
        self.rect = pygame.Rect(0, 0, ai_settings.alien_attack_width, ai_settings.alien_attack_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # store location with float
        self.y = float(self.rect.y)
        self.color = ai_settings.alien_attack_color
        self.speed = ai_settings.alien_attack_speed

    def update(self):
        """attack fly down"""
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        """draw alien attack on the screen"""  
        pygame.draw.rect(self.screen, self.color, self.rect)