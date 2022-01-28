import sys

import pygame

import ttt_settings as tt
import game_screens as gs

# Initialize pygame, settings, and screen object.
pygame.init()

game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
pygame.display.set_caption("Tic Tac Toe by Yerbulan!")


# Here we go, let's start with a start menu
gs.display_screen(game_settings, screen, "black", "Quit", "Start")


run_game()


