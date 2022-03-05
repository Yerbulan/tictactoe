"""This is the main file for TicTacToe the game"""

# importing the pygame module and other modules needed for the game
# check out each module's docstring to find out how they work and what they do
import pygame
import game_sequence as gsq
import ttt_settings as tt

# Initialize pygame, settings, and screen object.
pygame.init()
game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.
                                  screen_height))
# Below are the units that measure everything in the game. # w_u is one tenth
# of the width of the current screen and h_u is one tenth of the height. This
# allows for scaling for any window size (which can be changed in
# tt.Settings()), and also allows to easily imagine where the on screen
# objects will be when coding their positions. For example,the exact middle
# of the screen is: w_u*5, h_u*5
w_u = screen.get_width() / 10
h_u = screen.get_height() / 10

pygame.display.set_caption("Tic Tac Toe by Yerbulan!")

# This command launches the game. Open game_sequence to see how it works
gsq.start_screen(game_settings, screen, w_u, h_u)
