import sys

import pygame
from pygame.sprite import Group

import ttt_functions as tf
import ttt_settings as tt

# Initialize pygame, settings, and screen object.
pygame.init()

game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
pygame.display.set_caption("Tic Tac Toe by Yerbulan!")

tf.start_menu_screen(screen, game_settings)
tf.difficulty_screen(screen, game_settings)


def run_game():
	while True:
		tf.check_events()
		
		# IV. IF THE DIFFICULTY WAS CHOSEN CALL THE GAME MODULE WHERE OPPONENT IS A CLASS WITH THE RIGHT CLASS FOR THE DIFFICULTY LEVEL
		# V. IF THE GAME IS OVER (WIN, LOSE, OR DRAW) CALL THE GAME OVER MODULE WHICH RECORD THE RESULT AND LETS YOU CHOOSE TO START OVER (CHOOSE DIFFICULTY MODULE) OR EXIT
		
		# Redraw the screen during each pass through the loop.
		screen.fill(game_settings.bg_color_in_game)
		
		
		pygame.display.flip()

run_game()

