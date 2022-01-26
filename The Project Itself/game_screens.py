import sys

import pygame

import random

import ttt_functions as tf
import ttt_settings as tt

class game_screens():
    """ A class that stores basic characteristics of all possible game  screens"""

    def display_screen(screen, width, height, game_settings):
        # rendering a text written in font as defined in ttt_settings
        quit_text = game_settings.start_menu_font.render('quit', True, game_settings.font_color)
        start_text = game_settings.start_menu_font.render('start', True, game_settings.font_color)

        while True:

            screen.fill(game_settings.bg_color)

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the quit button the game is terminated
                    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.quit()

                    # if the mouse is clicked on the start button the game is started
                    if width / 3 <= mouse[0] <= width / 3 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                        return

            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # if mouse is hovered on a button it changes to lighter shade
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 2, 140, 40])

            else:
                pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 2, 140, 40])

            if width / 3 <= mouse[0] <= width / 3 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                pygame.draw.rect(screen, game_settings.color_light, [width / 3, height / 3, 140, 40])

            else:
                pygame.draw.rect(screen, game_settings.color_dark, [width / 3, height / 3, 140, 40])

            # superimposing the text onto our button
            screen.blit(quit_text, (width / 2 + 50, height / 2))
            screen.blit(start_text, (width / 3 + 50, height / 3))

            # updates the frames of the game
            pygame.display.update()