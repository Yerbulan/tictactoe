""" 
This module is reposnible for taking player input and responding to it by creating on-screen graphics
"""

import pygame


def create_display(game_settings, screen):
    screen.fill(game_settings.bg_color)


# displays text on a given screen with given coordinates
def create_onscreen_text(game_settings, screen, x, y, text, fontsize=None):
    if fontsize:
        onscreen_text = game_settings.x_o_font.render(text, True, game_settings.font_color)
        screen.blit(onscreen_text, (x, y))
    else:
        onscreen_text = game_settings.font.render(text, True, game_settings.font_color)
        screen.blit(onscreen_text, (x, y))


# creates a button on a given screen with given coordinates
# the button changes color when the mouse is hovered on it
# the button functions are coded separately in game_interactions.py
def create_button(game_settings, screen, x1, x2, y1, y2):
    mouse = pygame.mouse.get_pos()

    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
        pygame.draw.rect(screen, game_settings.color_active, [x1, y1, x2 - x1, y2 - y1])
    else:
        pygame.draw.rect(screen, game_settings.color_inactive, [x1, y1, x2 - x1, y2 - y1])


# creates a tictactie grid
def create_grid(game_settings, screen, w_u, h_u):
    pygame.draw.line(screen, game_settings.grid_color, (w_u * 2, h_u * 4), (w_u * 8, h_u * 4), 8)
    pygame.draw.line(screen, game_settings.grid_color, (w_u * 2, h_u * 6), (w_u * 8, h_u * 6), 8)
    pygame.draw.line(screen, game_settings.grid_color, (w_u * 4, h_u * 2), (w_u * 4, h_u * 8), 8)
    pygame.draw.line(screen, game_settings.grid_color, (w_u * 6, h_u * 2), (w_u * 6, h_u * 8), 8)


# creates a straight line over the winning combination
# not the most beautiful code, but it works
def create_finishline(game_settings, screen, w_u, h_u):
    if game_settings.current_win_combination:
        if game_settings.current_win_combination == {"[2, 4, 2, 4]", "[4, 6, 2, 4]", "[6, 8, 2, 4]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 1.95, h_u * 3.05), (w_u * 7.95, h_u * 3.05), 8)
        elif game_settings.current_win_combination == {"[2, 4, 4, 6]", "[4, 6, 4, 6]", "[6, 8, 4, 6]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 1.95, h_u * 5.05), (w_u * 7.95, h_u * 5.05), 8)
        elif game_settings.current_win_combination == {"[2, 4, 6, 8]", "[4, 6, 6, 8]", "[6, 8, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 1.95, h_u * 7.05), (w_u * 7.95, h_u * 7.05), 8)
        elif game_settings.current_win_combination == {"[2, 4, 2, 4]", "[2, 4, 4, 6]", "[2, 4, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 2.95, h_u * 2.05), (w_u * 2.95, h_u * 8.05), 8)
        elif game_settings.current_win_combination == {"[4, 6, 2, 4]", "[4, 6, 4, 6]", "[4, 6, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 4.95, h_u * 2.05), (w_u * 4.95, h_u * 8.05), 8)
        elif game_settings.current_win_combination == {"[6, 8, 2, 4]", "[6, 8, 4, 6]", "[6, 8, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 6.95, h_u * 2.05), (w_u * 6.95, h_u * 8.05), 8)
        elif game_settings.current_win_combination == {"[2, 4, 2, 4]", "[4, 6, 4, 6]", "[6, 8, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 2.95, h_u * 3.05), (w_u * 6.95, h_u * 7.05), 8)
        elif game_settings.current_win_combination == {"[6, 8, 2, 4]", "[4, 6, 4, 6]", "[2, 4, 6, 8]"}:
            pygame.draw.line(screen, game_settings.fincolor, (w_u * 6.95, h_u * 3.05), (w_u * 2.95, h_u * 7.05), 8)
    else:
        return
