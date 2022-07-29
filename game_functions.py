import pygame
import sys
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien
from ship import Ship
from time import sleep
from pygame import mixer
from red_alien import RedAlien
import random


# Responding to key down events
def check_key_down_events(event, ship, ai_settings, screen, bullet, aliens, stats, red_aliens, alien_bullets,
                          settings_button, play_button, main_menu, sb, settings_tab, settings_exit, screen_resolution, controls, exit_button):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_SPACE:
		fire_bullet(ship, ai_settings, screen, bullet)
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_p:
		check_key(ai_settings, screen, bullet, aliens, ship, stats, red_aliens, alien_bullets)
	if event.key == pygame.K_ESCAPE:
		main_menu_show(stats, settings_button, play_button, main_menu, ship, ai_settings, screen, bullet, aliens, sb,
					red_aliens, alien_bullets, settings_tab, settings_exit, screen_resolution, controls, exit_button)


# Responding to key up events
def check_key_up_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ship, ai_settings, screen, bullet, stats, play_button, aliens, sb, red_aliens, alien_bullets,
				settings_tab, settings_button, settings_exit, main_menu, screen_resolution, controls, exit_button):
	# Running game until user pres X
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Responding to user input
		elif event.type == pygame.KEYDOWN:
			check_key_down_events(event, ship, ai_settings, screen, bullet, aliens, stats, red_aliens, alien_bullets,
						settings_button, play_button, main_menu, sb, settings_tab, settings_exit, screen_resolution, controls, exit_button)

		elif event.type == pygame.KEYUP:
			check_key_up_events(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:

			mouse_x, mouse_y = pygame.mouse.get_pos()

			check_exit(exit_button, mouse_x, mouse_y, stats)
			check_play_button(ai_settings, screen, bullet, aliens, ship, stats, play_button, mouse_x, mouse_y, sb, red_aliens,
								alien_bullets)

			check_settings_button(ai_settings, screen, settings_tab, settings_button, mouse_x, mouse_y, stats,
								settings_exit, play_button, main_menu, ship, bullet, aliens, sb, red_aliens, alien_bullets, screen_resolution, controls, exit_button)

			exit_button_ = settings_exit.rect.collidepoint(mouse_x, mouse_y)
			if exit_button_:
				main_menu_show(stats, settings_button, play_button, main_menu, ship, ai_settings, screen, bullet,
								aliens, sb, red_aliens, alien_bullets, settings_tab, settings_exit, screen_resolution, controls, exit_button)


def check_key(ai_settings, screen, bullet, aliens, ship, stats, red_aliens, alien_bullets):
	if not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		aliens.empty()
		bullet.empty()
		red_aliens.empty()
		alien_bullets.empty()
		create_red_fleet(ai_settings, screen, red_aliens)
		create_fleet(ai_settings, screen, aliens)
		ship.remove()
		ship.center_ship()


def check_play_button(ai_settings, screen, bullet, aliens, ship, stats, play_button, mouse_x, mouse_y, sb, red_aliens,
						alien_bullets):

	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True
		sb.prep_level()
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_ships()
		aliens.empty()
		bullet.empty()
		alien_bullets.empty()
		create_red_fleet(ai_settings, screen, red_aliens)

		create_fleet(ai_settings, screen, aliens)
		ship.center_ship()


def check_exit(exit_button, mouse_x, mouse_y, stats):
	exit_game = exit_button.rect.collidepoint(mouse_x, mouse_y)
	if exit_game and not stats.game_active:
		sys.exit()

def check_settings_button(ai_settings, screen, settings_tab, settings_button, mouse_x, mouse_y, stats, settings_exit,
					play_button, main_menu, ship, bullet, aliens, sb, red_aliens, alien_bullets, screen_resolution,
					controls, exit_button):

	button_collide = settings_button.rect.collidepoint(mouse_x, mouse_y)

	if button_collide and not stats.game_active:

		while True:

			screen.fill(ai_settings.settings_color)
			settings_tab.show_settings()
			settings_exit.draw_button()
			screen_resolution.blit_resolution()
			screen_resolution.blit_resolution_menu()
			controls.blit_controls()
			if stats.game_active:
				break
			check_events(ship, ai_settings, screen, bullet, stats, play_button, aliens, sb, red_aliens, alien_bullets,
						settings_tab, settings_button, settings_exit, main_menu, screen_resolution, controls, exit_button)

			pygame.display.flip()


def main_menu_show(stats, settings_button, play_button, main_menu, ship, ai_settings, screen, bullet, aliens, sb,
					red_aliens, alien_bullets, settings_tab, settings_exit, screen_resolution, controls, exit_button):
	run_display = True
	while run_display:
		if stats.game_active:
			break
		check_events(ship, ai_settings, screen, bullet, stats, play_button, aliens, sb, red_aliens, alien_bullets, settings_tab, settings_button, settings_exit, main_menu, screen_resolution,
		             controls, exit_button)
		main_menu.show()
		settings_button.show_settings()
		play_button.draw_button()
		exit_button.show_exit()
		pygame.display.flip()



def get_number_rows(ai_settings, screen):
	ship = Ship(ai_settings, screen)
	alien = Alien(ai_settings, screen)
	ship_height = ship.image.get_height()
	alien_height = alien.rect.height
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (3 * alien_height))
	return number_rows


def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width  # (1200 - 2 * 60)... = 1080
	number_aliens_x = int(available_space_x / (2 * alien_width))  # (1080 / (2 * 60)... = 9
	return number_aliens_x


def get_number_red_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 4 * alien_width  # (1200 - 4 * 60)... =
	number_red_aliens_x = int(available_space_x / (2 * alien_width))
	return number_red_aliens_x


def create_red_alien(ai_settings, screen, red_aliens, red_alien_number):
	alien = Alien(ai_settings, screen)
	red_alien = RedAlien(screen, ai_settings)
	red_alien_width = red_alien.rect.width
	red_alien.x = red_alien_width + (2 * red_alien_width * red_alien_number)
	red_alien.rect.x = red_alien.x
	red_aliens.add(red_alien)
	red_alien.rect.y = 100


def create_red_fleet(ai_settings, screen, red_aliens):
	if ai_settings.screen_width == 1280:
		number_red_aliens_x = [1, 3, 5, 7]
		for red_alien_number in number_red_aliens_x:
			create_red_alien(ai_settings, screen, red_aliens, red_alien_number)
	if ai_settings.screen_width == 1920:
		number_red_aliens_x = [1, 3, 5, 7, 9, 11, 13]
		for red_alien_number in number_red_aliens_x:
			create_red_alien(ai_settings, screen, red_aliens, red_alien_number)



def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = int(1.5 * alien_width + (2 * alien_width * alien_number))  # (60 + 2 * 60 * 1(2, 3, 4, 5, 6, 7, 8, 9))
	alien.rect.x = alien.x
	aliens.add(alien)
	alien.rect.y = 200 + 2 * alien.rect.height * row_number


def create_fleet(ai_settings, screen, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, screen)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def fire_bullet(ship, ai_settings, screen, bullet):
	# Firing 3 bullets at the time
	if len(bullet) < ai_settings.bullets_allowed:
		bullet_sound = mixer.Sound('Music/laser (1).wav')
		bullet_sound.set_volume(0.2)
		bullet_sound.play()
		new_bullet = Bullet(ai_settings, screen, ship)
		bullet.add(new_bullet)


def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		filename = 'High score.txt'
		high_score = str(stats.high_score)
		with open(filename, 'w') as file_object:
			file_object.write(high_score)
		sb.prep_high_score()


def load_high_score(stats):
	filename = 'High score.txt'
	with open(filename) as file_object:
		l_high_score = file_object.read()
		stats.high_score = int(l_high_score)


def alien_shot(ai_settings, screen, red_aliens, alien_bullets):
	if len(alien_bullets) < ai_settings.bullets_allowed_alien:
		for red_alien in red_aliens:
			new_alien_bullet = AlienBullet(ai_settings, screen, red_alien)
			alien_bullets.add(new_alien_bullet)


def shot_again(ai_settings, screen, red_aliens, alien_bullets):
	alien_bullets.update()
	if random.randrange(0, 1000) == 1:
		alien_shot(ai_settings, screen, red_aliens, alien_bullets)
	for alien_bullet in alien_bullets.copy():
		if alien_bullet.rect.bottom >= ai_settings.screen_height:
			alien_bullets.remove(alien_bullet)


def alien_bullet_collision(bullet, aliens, ai_settings, screen, sb, stats, red_aliens, alien_bullets, ship):
	collision = pygame.sprite.groupcollide(bullet, aliens, True, True)
	red_aliens_collision = pygame.sprite.groupcollide(bullet, red_aliens, True, True)
	bullet_player_collision = pygame.sprite.spritecollideany(ship, alien_bullets)
	bullet_bullet_collision = pygame.sprite.groupcollide(bullet, alien_bullets, True, True)
	if collision:
		for aliens in collision.values():
			stats.score += ai_settings.alien_points * len(aliens)
			collision_sound = mixer.Sound('Music/explosion (1).wav')
			collision_sound.set_volume(0.1)
			collision_sound.play()
			sb.prep_score()

		check_high_score(stats, sb)
	if bullet_player_collision:
		ship_hit(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets)

	if red_aliens_collision:
		for red_aliens in red_aliens_collision.values():
			stats.score += ai_settings.red_alien_points * len(red_aliens)
			collision_sound = mixer.Sound('Music/explosion (1).wav')
			collision_sound.set_volume(0.1)
			collision_sound.play()
			sb.prep_score()
	if len(aliens) == 0 and len(red_aliens) == 0:
		ai_settings.increase_speed()
		bullet.empty()
		alien_bullets.empty()
		red_aliens.empty()
		aliens.empty()
		stats.level += 1
		sb.prep_level()
		create_red_fleet(ai_settings, screen, red_aliens)
		create_fleet(ai_settings, screen, aliens)


def update_bullets(bullet, aliens, ai_settings, screen, sb, stats, red_aliens, alien_bullets, ship):
	# Removing bullets when they hit top
	bullet.update()
	for bullet_1 in bullet.copy():
		if bullet_1.rect.bottom <= 0:
			bullet.remove(bullet_1)
	alien_bullet_collision(bullet, aliens, ai_settings, screen, sb, stats, red_aliens, alien_bullets, ship)



def update_screen(ai_settings, screen, ship, aliens, bullet, stats, play_button, sb, red_aliens, alien_bullets, main_menu, settings_button, settings_tab, settings_exit, screen_resolution, controls, exit_button):
	# Screen update
	screen.fill(ai_settings.bg_colors)
	ship.player()
	aliens.draw(screen)
	red_aliens.draw(screen)
	for bullet_1 in bullet.sprites():
		bullet_1.draw_bullet()
	for alien_bullet in alien_bullets.sprites():
		alien_bullet.draw_alien_bullet()
	sb.show_score()
	main_menu_show(stats, settings_button, play_button, main_menu, ship, ai_settings, screen, bullet, aliens, sb, red_aliens, alien_bullets, settings_tab, settings_exit, screen_resolution, controls, exit_button)
	pygame.display.flip()


def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_direction(ai_settings, aliens)
			break


def change_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_red_fleet_edges(ai_settings, red_aliens):
	for red_alien in red_aliens.sprites():
		if red_alien.check_edges():
			red_fleet_change_direction(ai_settings)
			break


def red_fleet_change_direction(ai_settings):
	ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets):
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		red_aliens.empty()
		bullet.empty()
		alien_bullets.empty()
		create_red_fleet(ai_settings, screen, red_aliens)
		create_fleet(ai_settings, screen, aliens)
		ship.center_ship()
		sleep(0.4)
		sb.prep_ships()

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_aliens(ai_settings, screen, aliens, ship, bullet, stats, sb, red_aliens, alien_bullets):
	for alien in aliens.sprites():
		if ship.screen_rect.bottom <= alien.rect.bottom:
			ship_hit(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets)
			break


def update_aliens(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	check_red_fleet_edges(ai_settings, red_aliens)
	red_aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets)
	check_aliens(ai_settings, screen, aliens, ship, bullet, stats, sb, red_aliens, alien_bullets)
