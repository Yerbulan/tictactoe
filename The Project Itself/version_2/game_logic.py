import random

import graphics as gs
import game_interactions as gi

import pygame

def decide_turn(game_settings):
	game_settings.players_turn = random.choice([True, False])

def check_turn(game_settings, screen, w_u, h_u):
	if game_settings.players_turn:
		players_turn(game_settings, screen, w_u, h_u)
	else:
		ai_turn(game_settings, screen, w_u, h_u)

def players_turn(game_settings, screen, w_u, h_u):
	while True:
		if game_settings.x_or_o_ == "x":
			xo = "X"
		else:
			xo = "O"
		for event in pygame.event.get():
			mouse = pygame.mouse.get_pos(event)
			gi.check_events(event)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if w_u*2 <= mouse[0] <= w_u*4 and h_u*2 <= mouse[1] <= h_u*4:
					gs.create_onscreen_text(game_settings, screen, w_u*2.6 , h_u*2.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)		
				elif w_u*4 <= mouse[0] <= w_u*6 and h_u*2 <= mouse[1] <= h_u*4:
					gs.create_onscreen_text(game_settings, screen, w_u*4.6 , h_u*2.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*6 <= mouse[0] <= w_u*8 and h_u*2 <= mouse[1] <= h_u*4:
					gs.create_onscreen_text(game_settings, screen, w_u*6.6 , h_u*2.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*2 <= mouse[0] <= w_u*4 and h_u*4 <= mouse[1] <= h_u*6:
					gs.create_onscreen_text(game_settings, screen, w_u*2.6 , h_u*4.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*4 <= mouse[0] <= w_u*6 and h_u*4 <= mouse[1] <= h_u*6:
					gs.create_onscreen_text(game_settings, screen, w_u*4.6 , h_u*4.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*6 <= mouse[0] <= w_u*8 and h_u*4 <= mouse[1] <= h_u*6:
					gs.create_onscreen_text(game_settings, screen, w_u*6.6 , h_u*4.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*2 <= mouse[0] <= w_u*4 and h_u*6 <= mouse[1] <= h_u*8:
					gs.create_onscreen_text(game_settings, screen, w_u*2.6 , h_u*6.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*4 <= mouse[0] <= w_u*6 and h_u*6 <= mouse[1] <= h_u*8:
					gs.create_onscreen_text(game_settings, screen, w_u*4.6 , h_u*6.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)	
				elif w_u*6 <= mouse[0] <= w_u*8 and h_u*6 <= mouse[1] <= h_u*8:
					gs.create_onscreen_text(game_settings, screen, w_u*6.6 , h_u*6.1, xo, 1)
					pygame.display.update()
					ai_turn(game_settings, screen, w_u, h_u)				
					
				
def ai_turn(game_settings, screen, w_u, h_u):
	print("Your turn")
	players_turn(game_settings, screen, w_u, h_u)
	




