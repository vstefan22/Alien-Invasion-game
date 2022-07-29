import pygame.font

class SettingsExit:
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 180, 40
		self.button_color = (148, 148, 148)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.Font('invasion.TTF', 35)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 20
		self.rect.y = self.screen_rect.top + 20

		self.prep_msg()

	def prep_msg(self):
		self.msg_image = self.font.render("Go back", True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = self.rect.x + 4
		self.msg_image_rect.y = self.rect.y

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, (self.msg_image_rect.x, self.msg_image_rect.y))