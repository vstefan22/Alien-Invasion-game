import pygame.font

class Button:
	def __init__(self, ai_settings, screen, msg):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 200, 50

		self.text_color = (255, 255, 255)
		self.font = pygame.font.Font('invasion.TTF', 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 20
		self.rect.y = self.screen_rect.centery - 70

		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, None)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = self.rect.x + 12
		self.msg_image_rect.y = self.rect.centery - 17

	def draw_button(self):

		self.screen.blit(self.msg_image, (self.msg_image_rect.x, self.msg_image_rect.y))
