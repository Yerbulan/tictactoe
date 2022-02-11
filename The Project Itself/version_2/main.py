"""This is the main file for TicTacToe the game"""

# importing the pygame module
import pygame

# A class in ttt_settings stores game settings, such as screen size, font colors, etc.
import ttt_settings as tt
# This module is responsible for displaying everything that's in the game. It doesn't do
# any logic or calculations, just gets called by other modules to display stuff
import graphics as gs
# This module is reposnible for taking player input and responding to it (by telling other modules to)
# calculate or display stuff
import game_interactions as gi
# This module is responsible for taking the player from screen to screen and killing previous processes so
# they stop working once there's no need for them.
# Check it out to see how the game works
import game_sequence as gsq

# Initialize pygame, settings, and screen object.
pygame.init()

# Let's initialize the settings. These can be changed in ttt_settings
game_settings = tt.Settings()
# Initilizes the first screen players are met with
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
# These are units that are used to measure everything in the game
# w_u is one tenth of the width current screen and h_u is one tenth of the height
# This allows for scaling for any window size (which can be changed in tt.Settings()), and also
# allows to easily imagine where the on screen objects will be when coding their positions -
# the exact middle of the screen is for example: w_u*5, h_u*5
w_u = screen.get_width() / 10
h_u = screen.get_height() / 10

pygame.display.set_caption("Tic Tac Toe by Yerbulan!")

# this is what launches the game. open game_sequence to see how it works
gsq.start_screen(game_settings, screen, w_u, h_u)
