# create screen where user can input the bet he wants to make
import pygame 
from buttons import *
from constants import *

pygame.init()

#bet display 1playergame
askforbet1 = font_size2.render('Player 1, click the box and make a bet!', True, dark_red)
askforbet1Rect = askforbet1.get_rect()
askforbet1Rect.topleft = (50, 90)    

disclaimer = font_size1.render('Your bet must be lower than 1000€. Enter a number between 1 and 999.', True, black)
disclaimerRect = disclaimer.get_rect()
disclaimerRect.topleft = (50, 120)  

#bet display 2playergame

#create user input: player makes a bet, can only input numbers
bet_player1 = ''
bet_player1Rect = pygame.Rect(50, 150, 120, 60)
color_active = dark_red
color_passive = dark_grey 
color = color_passive
valid_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
