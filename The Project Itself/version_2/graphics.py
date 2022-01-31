""" 
This module contains functions to display things on the screen on to create screens. No game logic, no settings, just creating stuff on the screen.
There should be different modules for simply calling screens and different ones for calling interactable or non-interactable screens

"""

import sys

import pygame

def create_display(screen, background_color):
	screen.fill(background_color)
	pygame.display.update()
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				exit()

		 
def create_onscreen_text(**kwargs):
	

# def create_interactable_buttons():

# def create_grid():

# def blip_o():

# def blip_x():

# def display_screen(game_settings, screen, background_color, **kwargs):
#     """
#         This is a screen constructor
#         You can specify background color, text to display, objects, to display, what those objects do when clicked, and so on.
#         The screen can be interactable or not
#         1. game_settings passes important game settings 
#         2. screen - takes a ready made pygame screen with set width and height and so on, 
#         3. background color is self explanatory
#         4. for kwargs give a list of words that need to be displayed as options on the screen (optional) (need to be strings) 
#             and list of box colors for those words (choose background color if no box is needed)
#     """
#     font = game_settings.start_menu_font 
#     font_color = game_settings.font_color
#     list_of_texts = []
#     list_of_colors = []
#     list_positions_y = []
#     # stores the width of the screen as defined in ttt_settings into a variable
#     width_unit = screen.get_width()/10
#     w_u = width_unit
#     # stores the height of the screen as defined in ttt_settings into a variable
#     height_unit = screen.get_height()/10
#     h_u = height_unit

#     if kwargs:
#         for text, color in kwargs.items():
#             current_text = font.render(text, True, font_color)
#             list_of_texts.append(current_text)
#             current_boxcolor = color
#             list_of_colors.append(current_boxcolor)
#             current_y_position = h_u*1 + list_positions_y(-1)


#     while True:
#         screen.fill(background_color)

#         for ev in pygame.event.get():

#             if ev.type == pygame.QUIT:
#                 pygame.quit()

#             # checks if a mouse is clicked
#             if ev.type == pygame.MOUSEBUTTONDOWN:

#                if kwargs:
#                     for text, color in kwargs.items():
                           
#                         # if the mouse is clicked on the quit button the game is terminated
#                         if w_u*5 <= mouse[0] <= w_u*5 + 140 and h_u*5 <= mouse[1] <= h_u*5 + 40:
#                             pygame.quit()

#                         # if the mouse is clicked on the start button the game is started
#                         if w_u*4 <= mouse[0] <= w_u*4 + 140 and h_u*3 <= mouse[1] <= h_u*3+ 40:
#                             return

#         # stores the (x,y) coordinates into the variable as a tuple
#         mouse = pygame.mouse.get_pos()

#         # if mouse is hovered on a button it changes to lighter shade
#         if w_u*5 <= mouse[0] <= w_u*5 + 140 and h_u*5 <= mouse[1] <= h_u*5 + 40:
#             pygame.draw.rect(screen, game_settings.color_light, [w_u*5, h_u*5, 140, 40])

#         else:
#             pygame.draw.rect(screen, list_of_colors[0], [w_u*5, h_u*5, 140, 40])

#         if w_u*4 <= mouse[0] <= w_u*4+ 140 and h_u*3 <= mouse[1] <= h_u*3 + 40:
#             pygame.draw.rect(screen, game_settings.color_light, [w_u*4, h_u*3, 140, 40])

#         else:
#             pygame.draw.rect(screen, list_of_colors[0], [w_u*4, h_u*3, 140, 40])

#         # superimposing the text onto our button
#         screen.blit(list_of_texts[0], (w_u*5 , h_u*5))
#         screen.blit(list_of_texts[1], (w_u*4 , h_u*3))

#         # updates the frames of the game
#         pygame.display.update()