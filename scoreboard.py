import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
	def __init__(self, screen, ai_settings, stats):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		self.text_color = (30, 30, 30)
		self.font = pygame.font.Font('invasion.TTF' , 30)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		rounded_score = int(round(self.stats.score, -1))
		score_str = "SCORE: "+"{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_colors)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left= self.screen_rect.left + 10
		self.score_rect.top = 10

	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = " HIGH SCORE: "+"{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_colors)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.top = self.score_rect.top
		self.high_score_rect.centerx = self.screen_rect.centerx

	def prep_level(self):
		level_str ="LEVEL: " + str(self.stats.level)
		self.level_image = self.font.render(str(level_str), True, self.text_color, self.ai_settings.bg_colors)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.score_rect.left
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x =  self.ai_settings.screen_width - ship.rect.width - ship_number * ship.rect.width - 10
			ship.rect.y = 8
			self.ships.add(ship)

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
