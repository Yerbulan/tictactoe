"""This module is responsible for taking the player from screen to screen and
killing previous processes so they stop working once there's no need for
them.
"""

import pygame
import game_interactions as gi
import game_logic as gl
import graphics as gs


# The first screen. Automatically closes the last one if the game was
# restarted. Gives the player options to start the game or to quit
def start_screen(game_settings, screen, w_u, h_u):
    while game_settings.start_screen_on:
        gs.create_display(game_settings, screen)
        gs.create_button(game_settings, screen, w_u * 1.8, w_u * 3, h_u * 2.8,
                         h_u * 3.6)
        gs.create_button(game_settings, screen, w_u * 1.8, w_u * 3, h_u * 4.3,
                         h_u * 5.1)
        gs.create_onscreen_text(game_settings, screen, w_u * 2, h_u * 3,
                                "START")
        gs.create_onscreen_text(game_settings, screen, w_u * 2, h_u * 4.5,
                                "QUIT")

        pygame.display.update()

        for event in pygame.event.get():
            gi.check_events(event)
            gi.quit_button(event, w_u * 1.8, w_u * 3, h_u * 4.3, h_u * 5.1)
            gi.start_button(game_settings, screen, w_u, h_u, event, w_u * 1.8,
                            w_u * 3, h_u * 2.8, h_u * 3.6)


# Second screen. Automatically closes the first one. Allows the player to
# choose difficulty level. Check out game_logic.py to see how game
# difficilties work
def choose_diff_screen(game_settings, screen, w_u, h_u):
    while game_settings.diff_screen_on:
        gs.create_display(game_settings, screen)
        gs.create_button(game_settings, screen, w_u * 3, w_u * 4.1, h_u * 2.8,
                         h_u * 3.6)
        gs.create_button(game_settings, screen, w_u * 3, w_u * 4.5, h_u * 3.8,
                         h_u * 4.6)
        gs.create_button(game_settings, screen, w_u * 3, w_u * 4.1, h_u * 4.8,
                         h_u * 5.6)
        gs.create_onscreen_text(game_settings, screen, w_u * 3.2, h_u * 3,
                                "EASY")
        gs.create_onscreen_text(game_settings, screen, w_u * 3.2, h_u * 4,
                                "NORMAL")
        gs.create_onscreen_text(game_settings, screen, w_u * 3.2, h_u * 5,
                                "HARD")

        pygame.display.update()

        for event in pygame.event.get():
            gi.check_events(event)
            gi.choose_diff_button(game_settings, screen, w_u, h_u, event)


# Third screen. Automatically closes the second one. Gives the player options
# to use either x or o
def choose_x_o(game_settings, screen, w_u, h_u):
    while game_settings.xo_screen_on:
        gs.create_display(game_settings, screen)
        gs.create_button(game_settings, screen, w_u * 3.3, w_u * 4.4, h_u *
                         2.8, h_u * 3.6)
        gs.create_button(game_settings, screen, w_u * 3.3, w_u * 4.4, h_u *
                         3.8, h_u * 4.6)
        gs.create_onscreen_text(game_settings, screen, w_u * 3.5,
                                h_u * 3, "X")
        gs.create_onscreen_text(game_settings, screen, w_u * 3.5,
                                h_u * 4, "O")

        pygame.display.update()

        for event in pygame.event.get():
            gi.check_events(event)
            gi.choose_x_o_button(game_settings, screen, w_u, h_u, event)


# Fourth screen. Automatically closes the third one. Gives the player options
# to use either x or o
def start_game(game_settings, screen, w_u, h_u):
    gl.decide_turn(game_settings)
    while game_settings.game_active:
        gs.create_display(game_settings, screen)
        gs.create_grid(game_settings, screen, w_u, h_u)

        for event in pygame.event.get():
            gi.check_events(event)
            gl.check_turn(game_settings, screen, w_u, h_u)

        pygame.display.update()


# Displays the resul of the game. Only option it gives is to click anywhere to
# proceed to the next screen
def game_result(game_settings, screen, w_u, h_u):
    while game_settings.game_result_screen:
        gs.create_finishline(game_settings, screen, w_u, h_u)
        gs.create_onscreen_text(game_settings, screen, w_u * 4.5, h_u * 0.5,
                                str(game_settings.result))
        gs.create_onscreen_text(game_settings, screen, w_u * 3.5, h_u * 1.25,
                                "Click anywhere to continue")

        for event in pygame.event.get():
            gi.check_events(event)
            gi.any_button_to_cont(game_settings, screen, w_u, h_u, event)
        pygame.display.update()


# Fifth screen. Automatically closes the fourth one. Gives the player options
# to restart the game/
# If the game is restarted, takes the player to the first screen
def game_over_screen(game_settings, screen, w_u, h_u):
    while not game_settings.game_active:
        gs.create_display(game_settings, screen)
        gs.create_button(game_settings, screen, w_u * 2.8, w_u * 5, h_u *
                         4.8, h_u * 5.6)
        gs.create_button(game_settings, screen, w_u * 5.8, w_u * 7, h_u *
                         4.8, h_u * 5.6)
        gs.create_onscreen_text(game_settings, screen, w_u * 3,
                                h_u * 5, "PLAY AGAIN")
        gs.create_onscreen_text(game_settings, screen, w_u * 6,
                                h_u * 5, "QUIT")

        pygame.display.update()

        for event in pygame.event.get():
            gi.check_events(event)
            gi.quit_button(event, w_u * 5.8, w_u * 7, h_u * 4.8, h_u * 5.6)
            gi.start_button(game_settings, screen, w_u, h_u, event, w_u * 2.8,
                            w_u * 5, h_u * 4.8, h_u * 5.6)
