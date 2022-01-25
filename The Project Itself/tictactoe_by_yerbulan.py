import sys

import pygame
from pygame.sprite import Group

import ttt_functions as tf
import ttt_settings as tt

# Initialize pygame, settings, and screen object.
pygame.init()

game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
# stores the width of the screen as defined in ttt_settings into a variable
width = screen.get_width()
# stores the height of the screen as defined in ttt_settings into a variable
height = screen.get_height()
pygame.display.set_caption("Tic Tac Toe by Yerbulan!")

tf.start_menu_screen(screen,width,height, game_settings)
tf.difficulty_screen(screen,width,height, game_settings)
tf.x_or_o(screen,width,height, game_settings)
screen.fill(game_settings.bg_color_in_game)



def run_game():
	game_active = True
	while game_active:
		
		tf.draw_board(screen,width,height, game_settings)
		tf.check_events(screen,width,height, game_settings)
				
		# V. IF THE GAME IS OVER (WIN, LOSE, OR DRAW) CALL THE GAME OVER MODULE WHICH RECORD THE RESULT AND LETS YOU CHOOSE TO START OVER (CHOOSE DIFFICULTY MODULE) OR EXIT
		
		# Redraw the screen during each pass through the loop.
		# pygame.display.flip()

run_game()


