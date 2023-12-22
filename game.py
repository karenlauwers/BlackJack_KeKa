import pygame
from constants import *

pygame.init() 

#set the playing field
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("BlackJack")

#deal the cards, place the cards in the playing field

#game loop
running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
    
    window.fill((casino_green1))
   
    pygame.display.update()

pygame.quit()

#calculate, check values to design a winner 
#score 





    




