from cProfile import run
from re import A, S

import pygame
from game_stats import GameStats
from setting import Settings
from ship import Ship
import game_function as gf 
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

# Done: write highest point into file before sys.exit()
# Done: refactor check_bullet_alien_collision(), create start_new_level()
# Done: refactor Scoreboard.__init__(), create prep_images()
# TODO: add shooting aboility for allien, add shield for ship
# TODO: add sound effect with pygame.mixer, like explosion sound and shooting sound

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Aien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    # stat of game
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # create new ship
    ship = Ship(screen=screen,ai_setting=ai_settings)
    # create bullet
    bullets = Group()
    aliens_bullets = Group()
    # create allien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens) 
 
    # main game loop
    while True:
        gf.check_events(ai_settings, screen,stats, sb, play_button, ship, aliens, bullets, aliens_bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_bullet(ai_settings, screen, stats, sb, ship, aliens, bullets) 
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)
        

run_game()
