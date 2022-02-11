"""
This module is responsinle for game ai and logic
"""
import random

import graphics as gs
import game_interactions as gi
import game_sequence as gsq

import pygame


# randomly decides who's turn it is once in the beginning of the game
def decide_turn(game_settings):
    game_settings.players_turn = random.choice([True, False])


# checks whether the game is over (through other function) and if not gives the turn to either AI
# or player, depending on whose turn it is
def check_turn(game_settings, screen, w_u, h_u):
    if game_settings.game_active == True:
        if game_settings.players_turn:
            players_turn(game_settings, screen, w_u, h_u)
        else:
            ai_turn(game_settings, screen, w_u, h_u)
    else:
        game_settings.game_active = False
        game_settings.game_result_screen = True
        game_settings.available_squares = [[2, 4, 2, 4], [4, 6, 2, 4], [6, 8, 2, 4], [2, 4, 4, 6], [4, 6, 4, 6],
                                           [6, 8, 4, 6], [2, 4, 6, 8], [4, 6, 6, 8], [6, 8, 6, 8]]
        game_settings.player_squares.clear()
        game_settings.ai_squares.clear()
        gsq.game_result(game_settings, screen, w_u, h_u)


# accepts input from player and ask graphics module to draw it on the screen
def players_turn(game_settings, screen, w_u, h_u):
    while game_settings.players_turn == True:
        if game_settings.x_or_o_ == "x":
            xo = "X"
        else:
            xo = "O"
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos(event)
            gi.check_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in game_settings.available_squares:
                    if w_u * square[0] <= mouse[0] <= w_u * square[1] and h_u * square[2] <= mouse[1] <= h_u * square[
                        3]:
                        game_settings.available_squares.remove(square)
                        game_settings.player_squares.add(str(square))
                        gs.create_onscreen_text(game_settings, screen, w_u * (square[0] + 0.6), h_u * (square[2] + 0.1),
                                                xo, 1)
                        pygame.display.update()
                        game_settings.players_turn = False
                        check_endgame(game_settings, screen, w_u, h_u)


# passes logic to either easy, normal, or dard ai, to determine which square to fill
def ai_turn(game_settings, screen, w_u, h_u):
    if game_settings.x_or_o_ == "x":
        xo = "O"
    else:
        xo = "X"
    if game_settings.diff_level == "easy":
        easy_ai(game_settings, screen, w_u, h_u, xo)
    elif game_settings.diff_level == "normal":
        normal_ai(game_settings, screen, w_u, h_u, xo)
    elif game_settings.diff_level == "hard":
        hard_ai(game_settings, screen, w_u, h_u, xo)


# simply fills in the next available square in the list
def easy_ai(game_settings, screen, w_u, h_u, xo):
    ai_turn = game_settings.available_squares.pop(0)
    game_settings.ai_squares.add(str(ai_turn))
    gs.create_onscreen_text(game_settings, screen, w_u * (ai_turn[0] + 0.6), h_u * (ai_turn[2] + 0.1), xo, 1)
    pygame.display.update()
    game_settings.players_turn = True
    check_endgame(game_settings, screen, w_u, h_u)


# fills in a random square from the available squares  list
def normal_ai(game_settings, screen, w_u, h_u, xo):
    ai_turn = random.choice(game_settings.available_squares)
    game_settings.available_squares.remove(ai_turn)
    game_settings.ai_squares.add(str(ai_turn))
    gs.create_onscreen_text(game_settings, screen, w_u * (ai_turn[0] + 0.6), h_u * (ai_turn[2] + 0.1), xo, 1)
    pygame.display.update()
    game_settings.players_turn = True
    check_endgame(game_settings, screen, w_u, h_u)


# slightly more complicated than easy and normal, asks another module below to calculate what square to fill in
def hard_ai(game_settings, screen, w_u, h_u, xo):
    ai_turn = calculate_hard_ai_turn(game_settings)
    game_settings.available_squares.remove(ai_turn)
    game_settings.ai_squares.add(str(ai_turn))
    gs.create_onscreen_text(game_settings, screen, w_u * (ai_turn[0] + 0.6), h_u * (ai_turn[2] + 0.1), xo, 1)
    pygame.display.update()
    game_settings.players_turn = True
    check_endgame(game_settings, screen, w_u, h_u)


# checks whether one of the game ending conditions is fulfilled (player won, AI won, or draw)
def check_endgame(game_settings, screen, w_u, h_u):
    for combination in game_settings.winning_combinations:
        if combination.issubset(game_settings.player_squares):
            game_settings.result = "YOU WIN!"
            game_settings.game_active = False
            game_settings.current_win_combination = combination
            check_turn(game_settings, screen, w_u, h_u)
        elif combination.issubset(game_settings.ai_squares):
            game_settings.result = "YOU LOST"
            game_settings.game_active = False
            game_settings.current_win_combination = combination
            check_turn(game_settings, screen, w_u, h_u)
    if not game_settings.available_squares:
        game_settings.result = "DRAW"
        game_settings.game_active = False
        game_settings.current_win_combination = None
        check_turn(game_settings, screen, w_u, h_u)
    check_turn(game_settings, screen, w_u, h_u)


# hard ai works as follows:
# first, it checks whether the player is a single step away from victory
# if so, it fills in the square that leads the player to victory, preventing them from winning
# if not, it check whether the AI is a single step away from victory
# if so, it fills in that square and wins
# if both conditions are false, it simply chooses a random square
# this code can be expanded to cover two steps ahead, but that would make winning against mathematically impossible
# here, the goal was to make the ai harded than "easy" and "normal", but not impossible to win against
def calculate_hard_ai_turn(game_settings):
    while True:
        for square in game_settings.available_squares:
            possible_player_squares = game_settings.player_squares.copy()
            possible_player_squares.add(str(square))
            for combination in game_settings.winning_combinations:
                if combination.issubset(possible_player_squares):
                    return square
        for square in game_settings.available_squares:
            possible_ai_squares = game_settings.ai_squares.copy()
            possible_ai_squares.add(str(square))
            for combination in game_settings.winning_combinations:
                if combination.issubset(possible_ai_squares):
                    return square
        square = random.choice(game_settings.available_squares)
        return square
