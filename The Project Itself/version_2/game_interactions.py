import pygame

import game_sequence as gsq

import ttt_settings as tt

def check_events(event):
	if event.type == pygame.QUIT:
		pygame.quit()
		exit()

def quit_button (event, x1, x2, y1, y2):
	mouse = pygame.mouse.get_pos(event)
	if event.type == pygame.MOUSEBUTTONDOWN:
		if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
			pygame.quit()
			exit()

def start_button (game_settings, screen, w_u, h_u, event, x1, x2, y1, y2):
	mouse = pygame.mouse.get_pos(event)
	if event.type == pygame.MOUSEBUTTONDOWN:
		if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
			game_settings.start_screen_on = False
			game_settings.game_active = True
			game_settings.diff_screen_on = True
			gsq.choose_diff_screen(game_settings, screen, w_u, h_u)

def choose_diff_button(game_settings, screen, w_u, h_u, event):
	mouse = pygame.mouse.get_pos(event)
	if event.type == pygame.MOUSEBUTTONDOWN:
		if w_u*3 <= mouse[0] <= w_u*4.1 and h_u*2.8 <= mouse[1] <= h_u*3.6:
			game_settings.diff_level = "easy"
			game_settings.diff_screen_on = False
			game_settings.xo_screen_on = True
			gsq.choose_x_o(game_settings, screen, w_u, h_u)			
		elif w_u*3 <= mouse[0] <= w_u*4.5 and h_u*3.8 <= mouse[1] <= h_u*4.6:
			game_settings.diff_level = "normal"
			game_settings.diff_screen_on = False
			game_settings.xo_screen_on = True
			gsq.choose_x_o(game_settings, screen, w_u, h_u)	
		elif w_u*3 <= mouse[0] <= w_u*4.1 and h_u*4.8 <= mouse[1] <= h_u*5.6:
			game_settings.diff_level = "hard"
			game_settings.diff_screen_on = False
			game_settings.xo_screen_on = True
			gsq.choose_x_o(game_settings, screen, w_u, h_u)	

def choose_x_o_button(game_settings, screen, w_u, h_u, event):
	mouse = pygame.mouse.get_pos(event)
	if event.type == pygame.MOUSEBUTTONDOWN:
		if w_u*3.3 <= mouse[0] <= w_u*4.4 and h_u*2.8 <= mouse[1] <= h_u*3.6:
			game_settings.x_or_o_ = "x"
			game_settings.xo_screen_on = False
			gsq.start_game(game_settings, screen, w_u, h_u)			
		elif w_u*3.3 <= mouse[0] <= w_u*4.4 and h_u*3.8 <= mouse[1] <= h_u*4.6:
			game_settings.x_or_o_ = "o"
			game_settings.xo_screen_on = False
			game_settings.game_over == False
			game_settings.game_active = True
			gsq.start_game(game_settings, screen, w_u, h_u)	

def any_button_to_cont(game_settings, screen, w_u, h_u, event):
	if event.type == pygame.MOUSEBUTTONDOWN:
		gsq.game_over_screen(game_settings, screen, w_u, h_u)



			


