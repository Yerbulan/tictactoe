import sys

import pygame

import random

def check_events(screen,width,height, game_settings):
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
			pc_turn()
			

def click_boxes(game_settings, screen, width,height, mouse):
	# if the mouse is clicked on the first square the square is filled
	if width/4 <= mouse[0] <= width/10*4 and height/10 <= mouse[1] <= height/10*3:
		draw_player(screen, game_settings, width/4+20, height/10*2+50)
	elif width/10*4 <= mouse[0] <= width/10*6 and height/10 <= mouse[1] <= height/10*3:
		draw_player(screen, game_settings, width/4+20, height/10*2+50)


def start_menu_screen(screen,width,height, game_settings):

	# rendering a text written in font as defined in ttt_settings
	quit_text = game_settings.start_menu_font.render('quit' , True , game_settings.font_color)
	start_text = game_settings.start_menu_font.render('start' , True , game_settings.font_color)

	while True:
		
		screen.fill(game_settings.bg_color)

		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
				
			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:
				
				#if the mouse is clicked on the quit button the game is terminated
				if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
					pygame.quit()

				#if the mouse is clicked on the start button the game is started
				if width/3 <= mouse[0] <= width/3+140 and height/3 <= mouse[1] <= height/3+40:
					return
					
		# stores the (x,y) coordinates into the variable as a tuple
		mouse = pygame.mouse.get_pos()
		
		# if mouse is hovered on a button it changes to lighter shade
		if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/2,140,40])
			
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/2,140,40])

		if width/3 <= mouse[0] <= width/3+140 and height/3 <= mouse[1] <= height/3+40:
			pygame.draw.rect(screen,game_settings.color_light,[width/3,height/3,140,40])
			
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/3,height/3,140,40])
		
		# superimposing the text onto our button
		screen.blit(quit_text , (width/2+50,height/2))
		screen.blit(start_text , (width/3+50,height/3))
		
		# updates the frames of the game
		pygame.display.update()

def difficulty_screen(screen, width,height, game_settings):

	# rendering a text written in font as defined in ttt_settings
	easy_dif_text = game_settings.start_menu_font.render('easy' , True , game_settings.font_color)
	normal_dif_text = game_settings.start_menu_font.render('normal' , True , game_settings.font_color)
	hard_dif_text = game_settings.start_menu_font.render('hard' , True , game_settings.font_color)

	while True:
		
		screen.fill(game_settings.bg_color)

		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
				
			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:
				
				#launches the game with different parameters depending on the chosen difficulty
				if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:
					#CHANGE THIS TO PROCEED WITH CERTAIN PARAMETERS LATER!
					return

				if width/2 <= mouse[0] <= width/2+140 and height/3+60 <= mouse[1] <= height/3+100:
					#CHANGE THIS TO PROCEED WITH CERTAIN PARAMETERS LATER!
					return

				if width/2 <= mouse[0] <= width/2+140 and height/3+120 <= mouse[1] <= height/3+160:
					#CHANGE THIS TO PROCEED WITH CERTAIN PARAMETERS LATER!
					return
					
		# stores the (x,y) coordinates into the variable as a tuple
		mouse = pygame.mouse.get_pos()
		
		# if mouse is hovered on a button it changes to lighter shade
		if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/3, 140,40])
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/3, 140,40])

		if width/2 <= mouse[0] <= width/2+140 and height/3+60 <= mouse[1] <= height/3+100:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/3+60, 140,40])
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/3+60, 140,40])

		if width/2 <= mouse[0] <= width/2+140 and height/3+120 <= mouse[1] <= height/3+160:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/3+120, 140,40])
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/3+120, 140,40])
		
		# superimposing the text onto our button
		screen.blit(easy_dif_text , (width/2,height/3))
		screen.blit(normal_dif_text, (width/2,height/3+60))
		screen.blit(hard_dif_text, (width/2,height/3+120))
		
		# updates the frames of the game
		pygame.display.update()

def x_or_o(screen,width,height, game_settings):

	# rendering a text written in font as defined in ttt_settings
	choose_x = game_settings.start_menu_font.render('X' , True , game_settings.font_color)
	choose_o = game_settings.start_menu_font.render('O' , True , game_settings.font_color)
	choose_turn_text = game_settings.start_menu_font.render('Choose either X or O. Turn order will be decided randomly.' , True , game_settings.font_color)
	choose_turn(game_settings)

	while True:
		
		screen.fill(game_settings.bg_color)

		screen.blit(choose_turn_text, (width/2-500,height/3-100))
		
		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()

			#checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:

				#determines whether the player is usin x's or o's
				if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:
					player_x = True
					return

				if width/2 <= mouse[0] <= width/2+140 and height/3+60 <= mouse[1] <= height/3+100:
					player_x = False
					return

		# stores the (x,y) coordinates into the variable as a tuple
		mouse = pygame.mouse.get_pos()
		
		# if mouse is hovered on a button it changes to lighter shade
		if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/3, 140,40])
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/3, 140,40])

		if width/2 <= mouse[0] <= width/2+140 and height/3+60 <= mouse[1] <= height/3+100:
			pygame.draw.rect(screen,game_settings.color_light,[width/2,height/3+60, 140,40])
		else:
			pygame.draw.rect(screen,game_settings.color_dark,[width/2,height/3+60, 140,40])

		# superimposing the text onto our button
		screen.blit(choose_x, (width/2,height/3))
		screen.blit(choose_o, (width/2,height/3+60))

		# updates the frames of the game
		pygame.display.update()

def draw_board(screen,width,height, game_settings):

	#drawing_the_board
	pygame.draw.line(screen,game_settings.color_white,(width/4,height/10*3), (width/2+width/4,height/10*3),8)
	pygame.draw.line(screen,game_settings.color_white,(width/4,height/10*6), (width/2+width/4,height/10*6),8)
	pygame.draw.line(screen,game_settings.color_white,(width/10*4,height/10), (width/10*4,height/10*8),8)
	pygame.draw.line(screen,game_settings.color_white,(width/10*6,height/10), (width/10*6,height/10*8),8)

	pygame.display.update()

def draw_player(screen, game_settings, x_pos, y_pos):
	"""" Draws either an x or an or or on a given surface and coordinates"""
	if player_x:
		pygame.draw.line(screen,game_settings.color_white,(x_pos, y_pos), (x_pos+100, y_pos-100),12)
		pygame.draw.line(screen, game_settings.color_white, (x_pos,  y_pos - 100), (x_pos + 100, y_pos), 12)
	else:
		pygame.draw.circle(screen,game_settings.color_white,(x_pos, y_pos), 12)
	
	pygame.display.update()

def choose_turn(game_settings):
	game_settings.players_turn = random.choice([True,False])
	return

def pc_turn():
	print("Yeah")

def player_input(game_settings, screen, width, height, mouse, event):
	if event.type == pygame.MOUSEBUTTONDOWN:
		click_boxes(game_settings, screen, width, height, mouse)





	




