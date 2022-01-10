import sys

import pygame
from pygame.sprite import Group

def check_events():
	"""Respond to keypresses."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	# I. HERE ADD COLOR OR A BACKGROUND IMAGE
	pygame.display.set_caption("Tic Tac Toe by Yerbulan!")
	while True:
		check_events()
		# II. HERE ADD OPTION TO EITHER QUIT OR START THE GAME
		# III. IF THE GAME IS STARTED CALL CHOOSE DIFFICULTY MODULE
		# IV. IF THE DIFFICULTY WAS CHOSEN CALL THE GAME MODULE WHERE OPPONENT IS A CLASS WITH THE RIGHT CLASS FOR THE DIFFICULTY LEVEL
		# V. IF THE GAME IS OVER (WIN, LOSE, OR DRAW) CALL THE GAME OVER MODULE WHICH RECORD THE RESULT AND LETS YOU CHOOSE TO START OVER (CHOOSE DIFFICULTY MODULE) OR EXIT
		
run_game()
