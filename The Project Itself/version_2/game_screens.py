""" 
This is a screen constructor
You can specify background color, text to display, objects, to display, what those objects do when clicked, and so on.
The screen can be interactable or not
"""

import sys

import pygame

def display_screen(game_settings, screen, background_color, *args):
    """
        1. game_settings passes important game settings 
        2. screen - takes a ready made pygame screen with set width and height and so on, 
        3. background color is self explanatory
        4. for args give a list of words that need to be displayed as options on the screen (optional) (need to be strings)
    """
    font = game_settings.start_menu_font 
    font_color = game_settings.font_color
    list_of_texts = []
    # stores the width of the screen as defined in ttt_settings into a variable
    width = screen.get_width()
    # stores the height of the screen as defined in ttt_settings into a variable
    height = screen.get_height()

    if args:
        for text in args:
            current_text = font.render(text, True, font_color)
            list_of_texts.append(current_text)


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
        screen.blit(list_of_texts[0], (width / 2 + 50, height / 2))
        screen.blit(list_of_texts[1], (width / 3 + 50, height / 3))

        # updates the frames of the game
        pygame.display.update()