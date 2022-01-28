import sys

import pygame

class Settings():
	"""A class to store all settings for TicTacToe."""

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (90, 145, 210)
		self.bg_color_in_game = (100, 135, 155)
		self.start_menu_font = pygame.font.SysFont('Corbel',35)
		self.font_color = (255,255,255)
		# light shade of the button
		self.color_light = (170,170,170)
		# dark shade of the button
		self.color_dark = (100,100,100)
		self.color_white = (255,255,255)
		self.players_turn = True
		self.player_x = False
		self.diff_level = 1
		self.available_squares = ["a1","a2","a3", "b1", "b2", "b3", "c1", "c2", "c3"]
		self.computers_squares = []
		self.players_squares = []