import sys

import pygame

class Settings():
	"""A class to store all settings for TicTacToe."""

	def __init__(self):
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		
		#screens on and off
		self.start_screen_on = True
		self.diff_screen_on = True
		self.xo_screen_on = True

		#game settings
		self.diff_level = None
		self.x_or_o_ = None
		self.players_turn = True 

		#colors and fonts
		self.bg_color = (100, 215, 240)
		self.font_color = (255,255,255)
		self.color_active = (60, 80, 100)
		self.color_inactive = (100, 215, 240)
		self.grid_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Corbel',35)
		self.x_o_font = pygame.font.SysFont('Corbel',180)

	
		# self.bg_color_in_game = (100, 135, 155)

		# self.color_white = (255,255,255)
		# 
	

		# self.available_squares = ["a1","a2","a3", "b1", "b2", "b3", "c1", "c2", "c3"]
		# self.computers_squares = []
		# self.players_squares = []