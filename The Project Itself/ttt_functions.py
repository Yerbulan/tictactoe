import sys

import pygame

def check_events():
	"""Respond to keypresses."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def start_menu_screen(screen, game_settings):

	# stores the width of the screen as defined in ttt_settings into a variable
	width = screen.get_width()

	# stores the height of the screen as defined in ttt_settings into a variable
	height = screen.get_height()

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

def difficulty_screen(screen, game_settings):

	# stores the width of the screen as defined in ttt_settings into a variable
	width = screen.get_width()

	# stores the height of the screen as defined in ttt_settings into a variable
	height = screen.get_height()

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



