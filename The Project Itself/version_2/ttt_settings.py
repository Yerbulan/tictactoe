# This module stores a single class for the tictactoe game

import pygame


class Settings:
    """A class to store all settings for TicTacToe."""

    def __init__(self):
        # screen size, feel free to change this, everything in the game will
        # scale accordingly
        self.screen_width = 1366
        self.screen_height = 768

        # screens on and off, these switches are needed to turn on and off
        # screens depending on
        # what's being used at the moment
        self.start_screen_on = True
        self.diff_screen_on = True
        self.xo_screen_on = True
        self.game_result_screen = True

        # settings for the gamemplay
        self.diff_level = None
        self.x_or_o_ = None

        # colors and fonts
        self.bg_color = (100, 215, 240)
        self.font_color = (255, 255, 255)
        self.color_active = (60, 80, 100)
        self.color_inactive = (100, 215, 240)
        self.grid_color = (255, 255, 255)
        self.fincolor = (190, 100, 100)
        self.font = pygame.font.SysFont('Corbel', 35)
        self.x_o_font = pygame.font.SysFont('Corbel', 180)

        # game_logic
        self.players_turn = True
        self.game_active = True
        self.available_squares = [[2, 4, 2, 4], [4, 6, 2, 4], [6, 8, 2, 4],
                                  [2, 4, 4, 6], [4, 6, 4, 6], [6, 8, 4, 6],
                                  [2, 4, 6, 8], [4, 6, 6, 8], [6, 8, 6, 8]]
        self.player_squares = set()
        self.ai_squares = set()
        self.game_over = False
        self.result = None
        self.current_win_combination = None
        self.winning_combinations = [
            {"[2, 4, 2, 4]", "[4, 6, 2, 4]", "[6, 8, 2, 4]"},
            {"[2, 4, 4, 6]", "[4, 6, 4, 6]", "[6, 8, 4, 6]"},
            {"[2, 4, 6, 8]", "[4, 6, 6, 8]", "[6, 8, 6, 8]"},
            {"[2, 4, 2, 4]", "[2, 4, 4, 6]", "[2, 4, 6, 8]"},
            {"[4, 6, 2, 4]", "[4, 6, 4, 6]", "[4, 6, 6, 8]"},
            {"[6, 8, 2, 4]", "[6, 8, 4, 6]", "[6, 8, 6, 8]"},
            {"[2, 4, 2, 4]", "[4, 6, 4, 6]", "[6, 8, 6, 8]"},
            {"[6, 8, 2, 4]", "[4, 6, 4, 6]", "[2, 4, 6, 8]"}
        ]
