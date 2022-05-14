from re import A
import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event,ai_settings, screen, stats, sb, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets,ai_settings,screen,ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        switch_bullet(ai_settings)
    elif event.key == pygame.K_p:
        start_newGame(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """response to keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y, ship, aliens, bullets)           

def update_screen(ai_settings, screen,stats, sb, ship, bullets, alien, play_button):
    """update image on the screen, and flip to new screen"""
    # update screen element
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    sb.show_score()

    # show button if game is not active
    if not stats.game_active:
        play_button.draw_button()
    
    # make new update visible
    pygame.display.flip()

def update_bullet(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update bullets location, delete vanished bullets"""
    bullets.update()
    # delete vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
def fire_bullet(bullets,ai_settings,screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a fleet of alien"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # create a row of alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
def get_number_aliens_x(ai_settings, alien_width):
    """determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +2 * alien.rect.height * row_number
    alien.y = float(alien.rect.y)
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows-3

def update_aliens(ai_settings,stats, screen, sb, ship, aliens, bullets):
    """update the position of aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check collision of alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_alien_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """respond to aliens reaching the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    """change the direction of the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def switch_bullet(ai_setting):
    """change bullet size and penatration"""
    if ai_setting.bullet_penatration:
        ai_setting.bullet_penatration = False
        ai_setting.bullet_width = 300
    else:
        ai_setting.bullet_penatration = True
        ai_setting.bullet_width = 3

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """responde to collision of bullet and alien"""
    # delete alien and bullet if bullets hit alien
    collision = pygame.sprite.groupcollide(bullets, aliens, ai_settings.bullet_penatration, True)

    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        # delete current bullets and create new fleet when all enemy die
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """response to ship hit by alien"""
    # -1 for ship_left
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        # clear all aliens and bulltes
        aliens.empty()
        bullets.empty()

        # create new fleet and ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause game
        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False

def check_alien_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """respond to alien hit the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # same result as alien hit the ship
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y,ship, aliens, bullets):
    """start game when player click button"""
    # reset stats
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_newGame(ai_settings, screen, stats, sb, ship, aliens, bullets)

def start_newGame(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """start new game"""
    stats.reset_stats()
    stats.game_active = True

    # reset score board image
    sb.prep_level()
    sb.prep_score()
    sb.prep_ships()

    # clear alien and bullets
    aliens.empty()
    bullets.empty()

    # reset settings
    ai_settings.initialize_dynamic_settings()

    # create new fleet and initialize ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # hide mouse
    pygame.mouse.set_visible(False)

def check_high_score(stats, sb):
    """check if current score the highest score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
