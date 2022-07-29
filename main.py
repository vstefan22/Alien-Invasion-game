import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame import mixer
from main_menu import MainMenu
from settings_button import SettingsButton
from settings_window import SettingsTab
from settings_exit_button import SettingsExit
from screen_resolution import Resolution
from controls import Controls
from exit import ExitButton

def run_game():
	# Game name and screen dimensions
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")
	icon = pygame.image.load('Images/ship.png')
	pygame.display.set_icon(icon)
	bullet = Group()
	aliens = Group()
	red_aliens = Group()
	alien_bullets = Group()

	ship = Ship(ai_settings, screen)
	settings_tab = SettingsTab(screen, ai_settings)
	settings_button = SettingsButton(ai_settings, screen)
	main_menu = MainMenu(screen, ai_settings)
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	settings_exit = SettingsExit(ai_settings, screen)
	screen_resolution = Resolution(ai_settings, screen)
	sb = Scoreboard(screen, ai_settings, stats)
	controls = Controls(ai_settings, screen)
	exit_button = ExitButton(ai_settings, screen)

	gf.create_fleet(ai_settings, screen, aliens)
	gf.create_red_fleet(ai_settings, screen, red_aliens)
	gf.load_high_score(stats)

	sb.prep_high_score()
	sb.prep_ships()
	sb.prep_score()
	sb.prep_level()

	pygame.mixer.pre_init(44100, -16, 2, 512)
	mixer.music.load('Music/background (1).wav')
	pygame.mixer.music.set_volume(0.25)
	mixer.music.play(-1)

	while True:
		# Running game until user pres X
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullet, aliens, ai_settings, screen, sb, stats, red_aliens, alien_bullets, ship)
			gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullet, sb, red_aliens, alien_bullets)
			gf.alien_bullet_collision(bullet, aliens, ai_settings, screen, sb, stats, red_aliens, alien_bullets, ship)
			gf.shot_again(ai_settings, screen, red_aliens, alien_bullets)
		alien_bullets.update()
		bullet.update()
		gf.check_events(ship, ai_settings, screen, bullet, stats, play_button, aliens, sb, red_aliens, alien_bullets, settings_tab, settings_button, settings_exit, main_menu, screen_resolution, controls, exit_button)
		gf.update_screen(ai_settings, screen, ship, aliens, bullet, stats, play_button, sb, red_aliens, alien_bullets, main_menu, settings_button, settings_tab, settings_exit, screen_resolution, controls, exit_button)


run_game()
