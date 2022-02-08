import random

import graphics as gs
import game_interactions as gi
import game_sequence as gsq

import pygame

def decide_turn(game_settings):
	game_settings.players_turn = random.choice([True, False])

def check_turn(game_settings, screen, w_u, h_u):
	if game_settings.game_active == True:
		if game_settings.players_turn:
			players_turn(game_settings, screen, w_u, h_u)
		else:
			ai_turn(game_settings, screen, w_u, h_u)
	else:
		game_settings.game_active = False
		game_settings.available_squares = [[2,4,2,4],[4,6,2,4],[6,8,2,4],[2,4,4,6],[4,6,4,6],[6,8,4,6],[2,4,6,8],[4,6,6,8],[6,8,6,8]]
		game_settings.player_squares.clear()
		game_settings.ai_squares.clear()
		gsq.game_result(game_settings, screen, w_u, h_u)

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
					if w_u*square[0] <= mouse[0] <= w_u*square[1] and h_u*square[2] <= mouse[1] <= h_u*square[3]:
						game_settings.available_squares.remove(square)
						game_settings.player_squares.add(str(square))
						gs.create_onscreen_text(game_settings, screen, w_u*(square[0]+0.6), h_u*(square[2]+0.1), xo, 1)
						pygame.display.update()
						game_settings.players_turn = False
						check_endgame(game_settings, screen, w_u, h_u)
									
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

def easy_ai(game_settings, screen, w_u, h_u, xo):
	ai_turn = game_settings.available_squares.pop(0)
	game_settings.ai_squares.add(str(ai_turn))
	gs.create_onscreen_text(game_settings, screen, w_u*(ai_turn[0]+0.6), h_u*(ai_turn[2]+0.1), xo, 1)
	pygame.display.update()
	game_settings.players_turn = True
	check_endgame(game_settings, screen, w_u, h_u)

def normal_ai(game_settings, screen, w_u, h_u, xo):
	ai_turn = random.choice(game_settings.available_squares)
	game_settings.available_squares.remove(ai_turn)
	game_settings.ai_squares.add(str(ai_turn))
	gs.create_onscreen_text(game_settings, screen, w_u*(ai_turn[0]+0.6), h_u*(ai_turn[2]+0.1), xo, 1)
	pygame.display.update()	
	game_settings.players_turn = True
	check_endgame(game_settings, screen, w_u, h_u)

def hard_ai(game_settings, screen, w_u, h_u, xo):
	ai_turn = random.choice(game_settings.available_squares)
	game_settings.available_squares.remove(ai_turn)
	game_settings.ai_squares.add(str(ai_turn))
	gs.create_onscreen_text(game_settings, screen, w_u*(ai_turn[0]+0.6), h_u*(ai_turn[2]+0.1), xo, 1)
	pygame.display.update()	
	game_settings.players_turn = True
	check_endgame(game_settings, screen, w_u, h_u)
	
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
		check_turn(game_settings, screen, w_u, h_u)
	check_turn(game_settings, screen, w_u, h_u)





