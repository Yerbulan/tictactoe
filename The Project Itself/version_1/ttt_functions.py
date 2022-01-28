import sys

import pygame

import random


def check_events(screen, width, height, game_settings):
    """Respond to keypresses."""

    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # checks if a mouse is clicked
        if game_settings.players_turn:
            player_input(game_settings, screen, width, height, mouse, event)
        else:
            pc_turn(game_settings, screen, width, height, mouse, event)


def click_boxes(game_settings, screen, width, height, mouse):
    # if the mouse is clicked on the first square the square is filled
    if width / 4 <= mouse[0] <= width / 10 * 4 and height / 10 <= mouse[1] <= height / 10 * 3:
        the_move = "a1"
        draw_player(screen, game_settings, width / 4 + 30, height / 10 * 2 + 50, the_move)
    elif width / 10 * 4 <= mouse[0] <= width / 10 * 6 and height / 10 <= mouse[1] <= height / 10 * 3:
        the_move = "a2"
        draw_player(screen, game_settings, width / 10 * 4 + 70, height / 10 * 2 + 50, the_move)
    elif width / 10 * 6 <= mouse[0] <= width / 10 * 8 and height / 10 <= mouse[1] <= height / 10 * 3:
        the_move = "a3"
        draw_player(screen, game_settings, width / 10 * 6 + 30, height / 10 * 2 + 50, the_move)
    elif width / 4 <= mouse[0] <= width / 10 * 4 and height / 10 * 3 <= mouse[1] <= height / 10 * 6:
        the_move = "b1"
        draw_player(screen, game_settings, width / 4 + 30, height / 10 * 3 + 170, the_move)
    elif width / 10 * 4 <= mouse[0] <= width / 10 * 6 and height / 10 * 3 <= mouse[1] <= height / 10 * 6:
        the_move = "b2"
        draw_player(screen, game_settings, width / 10 * 4 + 70, height / 10 * 3 + 170, the_move)
    elif width / 10 * 6 <= mouse[0] <= width / 10 * 8 and height / 10 * 3 <= mouse[1] <= height / 10 * 6:
        the_move = "b3"
        draw_player(screen, game_settings, width / 10 * 6 + 30, height / 10 * 3 + 170, the_move)
    elif width / 4 <= mouse[0] <= width / 10 * 4 and height / 10 * 6 <= mouse[1] <= height / 10 * 8:
        the_move = "c1"
        draw_player(screen, game_settings, width / 4 + 30, height / 10 * 6 + 130, the_move)
    elif width / 10 * 4 <= mouse[0] <= width / 10 * 6 and height / 10 * 6 <= mouse[1] <= height / 10 * 8:
        the_move = "c2"
        draw_player(screen, game_settings, width / 10 * 4 + 70, height / 10 * 6 + 130, the_move)
    elif width / 10 * 6 <= mouse[0] <= width / 10 * 8 and height / 10 * 6 <= mouse[1] <= height / 10 * 8:
        the_move = "c3"
        draw_player(screen, game_settings, width / 10 * 6 + 30, height / 10 * 6 + 130, the_move)


def start_menu_screen(screen, width, height, game_settings):
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


def difficulty_screen(screen, width, height, game_settings):
    # rendering a text written in font as defined in ttt_settings
    easy_dif_text = game_settings.start_menu_font.render('easy', True, game_settings.font_color)
    normal_dif_text = game_settings.start_menu_font.render('normal', True, game_settings.font_color)
    hard_dif_text = game_settings.start_menu_font.render('hard', True, game_settings.font_color)

    while True:

        screen.fill(game_settings.bg_color)

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # launches the game with different parameters depending on the chosen difficulty
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                    game_settings.diff_level = 1
                    return

                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
                    game_settings.diff_level = 2
                    return

                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 120 <= mouse[1] <= height / 3 + 160:
                    game_settings.diff_level = 3
                    return

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3, 140, 40])

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3 + 60, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3 + 60, 140, 40])

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 120 <= mouse[1] <= height / 3 + 160:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3 + 120, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3 + 120, 140, 40])

        # superimposing the text onto our button
        screen.blit(easy_dif_text, (width / 2, height / 3))
        screen.blit(normal_dif_text, (width / 2, height / 3 + 60))
        screen.blit(hard_dif_text, (width / 2, height / 3 + 120))

        # updates the frames of the game
        pygame.display.update()


def x_or_o(screen, width, height, game_settings):
    # rendering a text written in font as defined in ttt_settings
    choose_x = game_settings.start_menu_font.render('X', True, game_settings.font_color)
    choose_o = game_settings.start_menu_font.render('O', True, game_settings.font_color)
    choose_turn_text = game_settings.start_menu_font.render(
        'Choose either X or O. Turn order will be decided randomly.', True, game_settings.font_color)
    choose_turn(game_settings)

    while True:

        screen.fill(game_settings.bg_color)

        screen.blit(choose_turn_text, (width / 2 - 500, height / 3 - 100))

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # determines whether the player is usin x's or o's
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                    game_settings.player_x = True
                    return

                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
                    game_settings.player_x = False
                    return

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3, 140, 40])

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3 + 60, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3 + 60, 140, 40])

        # superimposing the text onto our button
        screen.blit(choose_x, (width / 2, height / 3))
        screen.blit(choose_o, (width / 2, height / 3 + 60))

        # updates the frames of the game
        pygame.display.update()


def draw_board(screen, width, height, game_settings):
    # drawing_the_board
    pygame.draw.line(screen, game_settings.color_white, (width / 4, height / 10 * 3),
                     (width / 2 + width / 4, height / 10 * 3), 8)
    pygame.draw.line(screen, game_settings.color_white, (width / 4, height / 10 * 6),
                     (width / 2 + width / 4, height / 10 * 6), 8)
    pygame.draw.line(screen, game_settings.color_white, (width / 10 * 4, height / 10),
                     (width / 10 * 4, height / 10 * 8), 8)
    pygame.draw.line(screen, game_settings.color_white, (width / 10 * 6, height / 10),
                     (width / 10 * 6, height / 10 * 8), 8)

    pygame.display.update()


def draw_player(screen, game_settings, x_pos, y_pos, the_move):
    """" Draws either an x or an or or on a given surface and coordinates"""
    if (the_move) in game_settings.available_squares:
        game_settings.available_squares.remove(the_move)
        game_settings.players_squares.append(the_move)
        game_settings.players_turn = False
        if game_settings.player_x:
            pygame.draw.line(screen, game_settings.color_white, (x_pos, y_pos), (x_pos + 100, y_pos - 100), 12)
            pygame.draw.line(screen, game_settings.color_white, (x_pos, y_pos - 100), (x_pos + 100, y_pos), 12)
        else:
            pygame.draw.circle(screen, game_settings.color_white, (x_pos + 60, y_pos - 50), 70, width=12)

    pygame.display.update()


def choose_turn(game_settings):
    game_settings.players_turn = random.choice([True, False])
    return


def player_input(game_settings, screen, width, height, mouse, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        click_boxes(game_settings, screen, width, height, mouse)


def pc_turn(game_settings, screen, width, height, mouse, event):
    if game_settings.diff_level == 1:
        easy_ai(game_settings, screen, width, height, mouse, event)
    elif game_settings.diff_level == 2:
        normal_ai(game_settings)
    elif game_settings.diff_level == 2:
        hard_ai(game_settings)


def easy_ai(game_settings, screen, width, height, mouse, event):
    try:
        taken_by_pc = random.choice(game_settings.available_squares)
    except IndexError:
        game_over(screen, width, height, game_settings, "Draw!")
    else:
        game_settings.computers_squares.append(taken_by_pc)
        game_settings.available_squares.remove(taken_by_pc)

    draw_pc(game_settings, screen, width, height, mouse, event, taken_by_pc)

    print("Available = " + str(game_settings.available_squares))
    if not game_settings.available_squares:
        game_over(screen, width, height, game_settings, "Draw!")
    print("Players = " + str(game_settings.players_squares))
    if {"a1", "a2", "a3"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"b1", "b2", "b3"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"c1", "c2", "c3"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"a1", "b1", "c1"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"a2", "b2", "c2"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"a3", "b3", "c3"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"a1", "b2", "c3"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    elif {"a3", "b2", "c1"}.issubset(set(game_settings.players_squares)):
        game_over(screen, width, height, game_settings, "You win!")
    print("Computers = " + str(game_settings.computers_squares))
    if {"a1", "a2", "a3"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"b1", "b2", "b3"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"c1", "c2", "c3"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"a1", "b1", "c1"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"a2", "b2", "c2"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"a3", "b3", "c3"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"a1", "b2", "c3"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")
    elif {"a3", "b2", "c1"}.issubset(set(game_settings.computers_squares)):
        game_over(screen, width, height, game_settings, "You lose")

    print("Your turn!")
   


def game_over(screen, width, height, game_settings, message):
    # rendering a text written in font as defined in ttt_settings
    continue_game = game_settings.start_menu_font.render('Continue', True, game_settings.font_color)
    quit_game = game_settings.start_menu_font.render('Quit', True, game_settings.font_color)
    text_screen = game_settings.start_menu_font.render(message, True, game_settings.font_color)

    while True:

        screen.fill(game_settings.bg_color)

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # determines whether the player is usin x's or o's
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                    game_settings.available_squares = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
                    game_settings.computers_squares = []
                    game_settings.players_squares = []
                    return

                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
                    pygame.quit()

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3, 140, 40])

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 + 60 <= mouse[1] <= height / 3 + 100:
            pygame.draw.rect(screen, game_settings.color_light, [width / 2, height / 3 + 60, 140, 40])
        else:
            pygame.draw.rect(screen, game_settings.color_dark, [width / 2, height / 3 + 60, 140, 40])

        # superimposing the text onto our button
        screen.blit(continue_game, (width / 2, height / 3))
        screen.blit(quit_game, (width / 2, height / 3 + 60))
        screen.blit(text_screen, (width / 2 - 500, height / 3 - 100))

        # updates the frames of the game
        pygame.display.update()


def draw_pc(game_settings, screen, width, height, mouse, event, taken_by_pc):
    """" Draws either an x or an or or on a given surface and coordinates"""
    if taken_by_pc == "a1":
        x_pos = width / 4 + 30
        y_pos = height / 10 * 2 + 50
    elif taken_by_pc == "a2":
        x_pos = width / 10 * 4 + 70
        y_pos = height / 10 * 2 + 50
    elif taken_by_pc == "a3":
        x_pos = width / 10 * 6 + 30
        y_pos = height / 10 * 2 + 50
    elif taken_by_pc == "b1":
        x_pos = width / 4 + 30
        y_pos = height / 10 * 3 + 170
    elif taken_by_pc == "b2":
        x_pos = width / 10 * 4 + 70
        y_pos = height / 10 * 3 + 170
    elif taken_by_pc == "b3":
        x_pos = width / 10 * 6 + 30
        y_pos = height / 10 * 3 + 170
    elif taken_by_pc == "c1":
        x_pos = width / 4 + 30
        y_pos = height / 10 * 6 + 130
    elif taken_by_pc == "c2":
        x_pos = width / 10 * 4 + 70
        y_pos = height / 10 * 6 + 130
    elif taken_by_pc == "c3":
        x_pos = width / 10 * 6 + 30
        y_pos = height / 10 * 6 + 130

    if game_settings.player_x == False:
        pygame.draw.line(screen, game_settings.color_white, (x_pos, y_pos), (x_pos + 100, y_pos - 100), 12)
        pygame.draw.line(screen, game_settings.color_white, (x_pos, y_pos - 100), (x_pos + 100, y_pos), 12)
    else:
        pygame.draw.circle(screen, game_settings.color_white, (x_pos + 60, y_pos - 50), 70, width=12)

    
    pygame.display.update()

    game_settings.players_turn = True

