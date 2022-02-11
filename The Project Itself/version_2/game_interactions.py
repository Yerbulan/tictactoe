"""This module is responsible for taking the player from screen to screen and killing previous processes so
they stop working once there's no need for them.
Check it out to see how the game works"""

import pygame

import game_sequence as gsq

import ttt_settings as tt

# quit function, is always called on by new screens, so it is possible to quit without errors
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

# quit button, initiates "quit" when mouse is clicked on a square with given coordinates
#(given coordinates should be the same where "quit" button is displayed in graphics.py)
def quit_button(event, x1, x2, y1, y2):
    mouse = pygame.mouse.get_pos(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
            pygame.quit()
            exit()

# start button, launches "choose difficulty screen". closes start menu screen 
def start_button(game_settings, screen, w_u, h_u, event, x1, x2, y1, y2):
    mouse = pygame.mouse.get_pos(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
            game_settings.start_screen_on = False
            game_settings.game_active = True
            game_settings.diff_screen_on = True
            gsq.choose_diff_screen(game_settings, screen, w_u, h_u)

# three buttons. all launch "choose x or o screen". all close "choose difficulty screen" 
# game_ai difficulty in settings is changed depending on which difficulty is chosen
# this will result in different ai being called for ai_turn in game_logic.py
def choose_diff_button(game_settings, screen, w_u, h_u, event):
    mouse = pygame.mouse.get_pos(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if w_u * 3 <= mouse[0] <= w_u * 4.1 and h_u * 2.8 <= mouse[1] <= h_u * 3.6:
            game_settings.diff_level = "easy"
            game_settings.diff_screen_on = False
            game_settings.xo_screen_on = True
            gsq.choose_x_o(game_settings, screen, w_u, h_u)
        elif w_u * 3 <= mouse[0] <= w_u * 4.5 and h_u * 3.8 <= mouse[1] <= h_u * 4.6:
            game_settings.diff_level = "normal"
            game_settings.diff_screen_on = False
            game_settings.xo_screen_on = True
            gsq.choose_x_o(game_settings, screen, w_u, h_u)
        elif w_u * 3 <= mouse[0] <= w_u * 4.1 and h_u * 4.8 <= mouse[1] <= h_u * 5.6:
            game_settings.diff_level = "hard"
            game_settings.diff_screen_on = False
            game_settings.xo_screen_on = True
            gsq.choose_x_o(game_settings, screen, w_u, h_u)

# changes appropriate setting in game_settings
def choose_x_o_button(game_settings, screen, w_u, h_u, event):
    mouse = pygame.mouse.get_pos(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if w_u * 3.3 <= mouse[0] <= w_u * 4.4 and h_u * 2.8 <= mouse[1] <= h_u * 3.6:
            game_settings.x_or_o_ = "x"
            game_settings.xo_screen_on = False
            gsq.start_game(game_settings, screen, w_u, h_u)
        elif w_u * 3.3 <= mouse[0] <= w_u * 4.4 and h_u * 3.8 <= mouse[1] <= h_u * 4.6:
            game_settings.x_or_o_ = "o"
            game_settings.xo_screen_on = False
            game_settings.game_over == False
            game_settings.game_active = True
            gsq.start_game(game_settings, screen, w_u, h_u)

#launches game restart sequence after game over
def any_button_to_cont(game_settings, screen, w_u, h_u, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        gsq.game_over_screen(game_settings, screen, w_u, h_u)
