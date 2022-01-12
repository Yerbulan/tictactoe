import sys

import pygame

class Settings():
	"""A class to store all settings for TicTacToe."""

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (90, 145, 210)
		self.bg_color_in_game = (5, 230, 230)
		self.start_menu_font = pygame.font.SysFont('Corbel',35)
		self.font_color = (255,255,255)
		# light shade of the button
		self.color_light = (170,170,170)
		# dark shade of the button
		self.color_dark = (100,100,100)