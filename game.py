import pygame
from buttons import *
from constants import *

pygame.init() 

#set the playing field
pygame.display.set_caption("BlackJack")

#welcome display 
welcome = font_size2.render('Welcome to BlackJack', True, dark_red)
welcomeRect = welcome.get_rect() 
welcomeRect.center = (window_width//2, window_height-500)

   
#game loop
running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
    
    window.fill((casino_green1))
    window.blit(welcome,welcomeRect)
    button_1player = Button('1 player',280, 150, True, 150, 50)
    button_2player = Button('2 players', 280, 220, True, 150, 50)


    pygame.display.update()

pygame.quit()

#calculate, check values to design a winner 
#score 





    




