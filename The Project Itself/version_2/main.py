import sys

import pygame

import ttt_settings as tt
import graphics as gs

# Initialize pygame, settings, and screen object.
pygame.init()

game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
pygame.display.set_caption("Tic Tac Toe by Yerbulan!")
not_started = True


def start_screen():
	while not_started:
		gs.create_display(screen, game_settings.bg_color)
		
		
start_screen()


