import sys

import pygame

import ttt_settings as tt
import graphics as gs
import game_interactions as gi
import game_sequence as gsq

# Initialize pygame, settings, and screen object.
pygame.init()

game_settings = tt.Settings()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
w_u = screen.get_width()/10
h_u = screen.get_height()/10

pygame.display.set_caption("Tic Tac Toe by Yerbulan!")

gsq.start_screen(game_settings, screen, w_u, h_u)

