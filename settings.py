class Settings:

	def __init__(self):
		self.screen_width = 1280
		self.settings()
	def settings(self):
		if self.screen_width == 1920:
			self.screen_height = 1080
		if self.screen_width == 1280:
			self.screen_height = 800
		self.bg_colors = (233, 233, 233)
		self.settings_color = (128, 128, 128)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_color = 60, 60, 60
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullets_allowed = 3

		# Alien bullet settings
		self.alien_bullet_color = 251, 43, 20
		self.alien_bullet_width = 4
		self.alien_bullet_height = 15
		self.bullets_allowed_alien = 2
		self.alien_bullet_speed = 1.3

		# Aliens fleet speed
		self.fleet_speed = 0.6
		self.fleet_drop_speed = 5.5

		self.speedup_scale = 1.07
		self.initialize_dynamic_settings()

		# Scoring
		self.alien_points = 50
		self.red_alien_points = 100
		self.score_scale = 1.5

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.8
		self.bullet_speed = 3.2
		self.alien_speed = 1
		self.fleet_direction = 1
		self.red_alien_speed= 0.7

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.red_alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
