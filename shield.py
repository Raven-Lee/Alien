import pygame

class Shield():
    def __init__(self, ai_settings, screen, ship) -> None:
        """init shield"""
        self.screen = screen

        # init a rect for shield at (0,0), then move above ship
        self.rect = pygame.Rect(0, 0, ai_settings.shield_width, ai_settings.shield_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.color = ai_settings.shield_color
        self.defense = 3
                
    def update(self, ship):
        """sheidl follow the ship"""
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

    def draw(self):
        """draw sheild on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)