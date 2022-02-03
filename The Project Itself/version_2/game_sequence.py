import pygame

import ttt_settings as tt
import graphics as gs
import game_interactions as gi
import game_logic as gl

def start_screen(game_settings, screen, w_u, h_u):
	while game_settings.start_screen_on == True:
		
		gs.create_display(game_settings, screen)
		gs.create_button(game_settings, screen, w_u*1.8, w_u*3, h_u*2.8, h_u*3.6)
		gs.create_button(game_settings, screen, w_u*1.8, w_u*3, h_u*4.3, h_u*5.1)
		gs.create_onscreen_text(game_settings, screen, w_u*2 , h_u*3, "START")
		gs.create_onscreen_text(game_settings, screen, w_u*2 , h_u*4.5, "QUIT")
						
		pygame.display.update()

		for event in pygame.event.get():
			gi.check_events(event)
			gi.quit_button (event, w_u*1.8, w_u*3, h_u*4.3, h_u*5.1)
			gi.start_button (game_settings, screen, w_u, h_u, event, w_u*1.8, w_u*3, h_u*2.8, h_u*3.6)

def choose_diff_screen(game_settings, screen, w_u, h_u):
	while game_settings.diff_screen_on == True:
		gs.create_display(game_settings, screen)
		gs.create_button(game_settings, screen, w_u*3, w_u*4.1, h_u*2.8, h_u*3.6)
		gs.create_button(game_settings, screen, w_u*3, w_u*4.5, h_u*3.8, h_u*4.6)
		gs.create_button(game_settings, screen, w_u*3, w_u*4.1, h_u*4.8, h_u*5.6)
		gs.create_onscreen_text(game_settings, screen, w_u*3.2 , h_u*3, "EASY")
		gs.create_onscreen_text(game_settings, screen, w_u*3.2 , h_u*4, "NORMAL")
		gs.create_onscreen_text(game_settings, screen, w_u*3.2 , h_u*5, "HARD")

		pygame.display.update()

		for event in pygame.event.get():
			gi.check_events(event)
			gi.choose_diff_button(game_settings, screen, w_u, h_u, event)

def choose_x_o(game_settings, screen, w_u, h_u):
	while game_settings.xo_screen_on == True:
		gs.create_display(game_settings, screen)
		gs.create_button(game_settings, screen, w_u*3.3, w_u*4.4, h_u*2.8, h_u*3.6)
		gs.create_button(game_settings, screen, w_u*3.3, w_u*4.4, h_u*3.8, h_u*4.6)
		gs.create_onscreen_text(game_settings, screen, w_u*3.5 , h_u*3, "X")
		gs.create_onscreen_text(game_settings, screen, w_u*3.5 , h_u*4, "O")

		pygame.display.update()

		for event in pygame.event.get():
			gi.check_events(event)
			gi.choose_x_o_button(game_settings, screen, w_u, h_u, event)

def start_game(game_settings, screen, w_u, h_u):
	while True:
		gl.decide_turn(game_settings)
		gs.create_display(game_settings, screen)
		gs.create_grid(game_settings, screen, w_u, h_u)
		
		for event in pygame.event.get():
			mouse = pygame.mouse.get_pos(event)
			gi.check_events(event)
			gl.check_turn(game_settings, screen, w_u, h_u)
		
		pygame.display.update()

		
			
	

		

			

# def game_over()