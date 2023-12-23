import pygame
from buttons import *
from constants import *
from bet import * 

pygame.init() 

#set the playing field
pygame.display.set_caption("BlackJack")

#welcome display 
welcome = font_size3.render('Welcome to BlackJack', True, dark_red)
welcomeRect = welcome.get_rect() 
welcomeRect.center = (window_width//2, 90)

#game loop
running = True
click_button_1player = False  # hulpvariabele om na te gaan of de button_1player geklikt wordt: onderdeel van de game loop
active_betRect = False  # hulpvariabele om na te gaan of player in de bet rectangle staat. Doel: om een bet te kunnen schrijven in de betRect moet je in die rectangle staat (en er op klikt). Het is niet nodig om te verwijzen naar speler 1 of speler 2 want je kan de variabele voor beiden inzetten. Denk ik.

while running:
    # clock.tick(fps)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

    # event: player clicks on button_1player, see further for the screen that will appear 
      if event.type == pygame.MOUSEBUTTONDOWN and button_1player.check_click(): 
         click_button_1player = True 

    # event: player inputs bet; player can only set input to the bet rectangle if he clicks on it 
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if bet_player1Rect.collidepoint(event.pos): 
          active_betRect = True
        else: 
          active_betRect = False

    # event: player inputs bet; player can only use numbers and backspace to return and delete charachters
      if active_betRect == True: 
        if event.type == pygame.KEYDOWN: 
          if event.key == pygame.K_BACKSPACE:  # define use of the backspace 
            bet_player1 = bet_player1[:-1] 
          elif bet_player1[:1] == '0':  # input cannot start with or be 0
            bet_player1 = bet_player1[:-1]           
          elif event.key in valid_keys and len(bet_player1)<3: #valid_keys is defined in bet.py = only number-keys
            bet_player1 += event.unicode
                       
      #set the main window, fill with colour 
      window.fill((casino_green1))

      #set the welcome screen with choice 1 or 2playergame
      window.blit(welcome,welcomeRect)
      button_1player = Button('1 player',280, 150, True, 150, 50)
      button_2player = Button('2 players', 280, 220, True, 150, 50)

    pygame.display.update()

  # displaying a new screen if the player clicks the button_1player, the event was introduced in the game loop (zie hoger)
    if click_button_1player: 
      window.fill((casino_green1))
      window.blit(askforbet1, askforbet1Rect)
      window.blit(disclaimer, disclaimerRect)

      if active_betRect: 
        color = color_active
      else: 
        color = color_passive 
      
      pygame.draw.rect(window, color, bet_player1Rect, 2)
      bet_surface = font_size4.render(bet_player1, True, dark_red)
      window.blit(bet_surface, (bet_player1Rect.x +5, bet_player1Rect.y+5))
  
    pygame.display.update()

pygame.quit()


#calculate, check values to design a winner 
#score 