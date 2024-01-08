import pygame 
from constants import dark_red, dark_grey

pygame.init()

# User input: player's name to use in f-strings during the game. Application in game.py. 
nameinput_player = ''
nameinput_playerRect = pygame.Rect(320, 220, 140, 40)

# User input: bet
betinput_player = ''
betinput_playerRect = pygame.Rect(340, 200, 120, 40)
color_active = dark_red
color_passive = dark_grey 
color = color_passive
valid_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]