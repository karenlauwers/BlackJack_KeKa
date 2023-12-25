import pygame, sys 

# IMPORT ALL FILES THAT CONTRIBUTE TO THE GAME LOOP AND THE WINDOW SETTINGS
from constants import *
from buttons import *
from user_input import * 
from gametext import * 

# INITIALISE PYGAME
pygame.init() 

# SET THE PLAYING FIELD
pygame.display.set_caption("BlackJack")

# AID VARIABLES. To help set the game loop and window settings. 

running = True
click_button_1player = False  # hulpvariabele om na te gaan of de button_1player geklikt wordt: onderdeel van de game loop
click_button_2player = False 
oneplayergame = False
twoplayergame = False 
active_betRect1 = False  # hulpvariabele om na te gaan of player in de bet rectangle staat. Doel: om een bet te kunnen schrijven in de betRect moet je in die rectangle staat (en er op klikt). Het is niet nodig om te verwijzen naar speler 1 of speler 2 want je kan de variabele voor beiden inzetten. Denk ik.
active_betRect2 = False 
click_bet_ok1 = False 
click_bet_ok2 = False 
click_play = False 

# GAME LOOP 
while running:
  # clock.tick(fps)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

  # EVENT IN WELCOME WINDOW. Player clicks on button_1player
    if event.type == pygame.MOUSEBUTTONDOWN and button_1player.check_click(): 
         click_button_1player = True 
             
    if event.type == pygame.MOUSEBUTTONDOWN and button_2player.check_click(): 
        click_button_2player = True

  # EVENT IN BET WINDOW. Player clicks on bet-rectangle and will be able to input bet. 
    if event.type == pygame.MOUSEBUTTONDOWN: 
      if betinput_player1Rect.collidepoint(event.pos): 
        active_betRect1 = True
      else: 
        active_betRect1 = False

      if betinput_player2Rect.collidepoint(event.pos): 
        active_betRect2 = True
      else: 
        active_betRect2 = False

  # EVENT IN BET WINDOW. Player inputs bet; player can only use numbers and backspace to return and delete charachters
    if active_betRect1 == True: 
      active_betRect2 == False 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # define use of the backspace 
          betinput_player1 = betinput_player1[:-1] 
        elif betinput_player1[:1] == '0':  # input cannot start with 0
          betinput_player1 = betinput_player1[:-1]           
        elif event.key in valid_keys and len(betinput_player1)<3: #valid_keys is defined in bet.py = only number-keys
          betinput_player1 += event.unicode

    if active_betRect2 == True: 
      active_betRect1 == False 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # define use of the backspace 
          betinput_player2 = betinput_player2[:-1] 
        elif betinput_player2[:1] == '0':  # input cannot start with 0
          betinput_player2 = betinput_player2[:-1]           
        elif event.key in valid_keys and len(betinput_player2)<3: #valid_keys is defined in bet.py = only number-keys
          betinput_player2 += event.unicode 
      
    # EVENT IN BET WINDOW. Player clicks ok 
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok1.check_click():
      click_bet_ok1 = True 
    
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok2.check_click():
      click_bet_ok2 = True 

    # EVENT IN BET WINDOW. Player clicks play in the bet-screen in the 1playergame.
    if event.type == pygame.MOUSEBUTTONDOWN and play.check_click(): 
      click_play = True 

# SETTING (DRAWING AND BLITTING) THE WINDOWS 
  # SET THE MAIN WINDOW. Fill with colour 
  window.fill((casino_green1))

  # SET THE WELCOME WINDOW. With choice 1 or 2playergame
  welcome.draw_text('center', window_width/2, 90)
  button_1player.draw_button()
  button_2player.draw_button()

  # EVENTUEEL IN TE VOEGEN # SET THE ASK-FOR-NAME WINDOW


  # SET THE BET WINDOW.
  # Set text and buttons 
  # Start by setting the screen for 1- and 2-player game 
  if click_button_1player or click_button_2player : 
    window.fill((casino_green1))
    bet_text.draw_text('topleft', 50, 90)  
    disclaimer.draw_text('topleft',50, 120)
    explanation.draw_text('topleft', 50, 140)
    player1.draw_text('topleft', 50, 190)
    bet_ok1.draw_button()
    player2.draw_text('topleft', 50, 300)
    bet_ok2.draw_button()
    play.draw_button()

    # Draw the textboxes in which the players are going to put their bet. 
      # The color of the box is red when the box is active and can be modified; grey when it isn't. 
      # First define the colors 
    if active_betRect1: 
      color1 = color_active
      color2 = color_passive
      active_betRect2 = False 
    else: 
      color1 = color_passive 

    if active_betRect2: 
        color2 = color_active
        color1 = color_passive
        active_betRect1 = False 
    else: 
        color2 = color_passive 

      # Then draw the textboxes
    pygame.draw.rect(window, color1, betinput_player1Rect, 2, 5)
    bet_surface = font_size2.render(betinput_player1, True, white)
    window.blit(bet_surface, (betinput_player1Rect.x+10, betinput_player1Rect.y+10))

    pygame.draw.rect(window, color2, betinput_player2Rect, 2, 5)
    bet_surface = font_size2.render(betinput_player2, True, white)
    window.blit(bet_surface, (betinput_player2Rect.x+10, betinput_player2Rect.y+10))
  
  if click_button_1player: 
    oneplayergame = True 
    twoplayergame = False 

  elif click_button_2player: 
    oneplayergame = False 
    twoplayergame = True 

  # BET WINDOW FOR 1PLAYERGAME
  if oneplayergame: 
    # for 1playergame: hide the player2-part by partly filling the screen. 
    window.fill((casino_green1), rect=(0,270, 400,230)) 
    # disable the buttons of the previous screen (welcome window with 1- or 2playergamebuttons). 
    # If you don't, you can still accidently click on them (even if they're not exposed.)
    button_1player.enabled = False 
    button_2player.enabled = False 

    # Setings for the play-button: you can only click play if you entered a bet between 1 and 999.
    if betinput_player1 =='0' or len(betinput_player1)<1: 
      bet_ok1.enabled = False 
      bet_ok1.draw_button()
    else: 
      bet_ok1.enabled = True 
      bet_ok1.draw_button() 
    
    if click_bet_ok1: 
      play.enabled = True 

  # BET WINDOW FOR 2-PLAYERGAME 
  if twoplayergame: 
    # Settings for the text and buttons for the bet-window in 2-playergame
    # Player 1 is asked to place his bet. Player 2 cannot enter his textbox. 
    betplease.draw_text('topleft', 380, 190)
    active_betRect2 = False 
    # Disable the buttons of the previous screen (welcome window with 1- or 2playergamebuttons). 
    # If you don't, you can still accidently click on them (even if they're not exposed).
    button_1player.enabled = False 
    button_2player.enabled = False     
    
    # If player 1 clicks the textbox, he can enter his bet. Player 2 cannot enter his box -  color is grey.
    if active_betRect1: 
      if betinput_player1 =='0' or len(betinput_player1)<1: 
        bet_ok1.enabled = False 
        bet_ok1.draw_button()
      else: 
        bet_ok1.enabled = True 
        bet_ok1.draw_button() 
    
    # If player 1 has clicked ok, the 'please bet' moves to player 2 and the color 
    if click_bet_ok1: 
      betplease.draw_text('topleft', 380, 300)
      window.fill((casino_green1), rect=(380,190, 200,50)) 
      player1.color = dark_grey
      player1.draw_text('topleft', 50, 190)
      player2.color = dark_red
      player2.draw_text('topleft', 50, 300)
      active_betRect1 = False 
      active_betRect2 = True 
      bet_ok1.enabled = False 
      bet_ok1.draw_button()
      if active_betRect2: 
        if betinput_player2 =='0' or len(betinput_player2)<1: 
          bet_ok2.enabled = False 
          bet_ok2.draw_button()
        else: 
          bet_ok2.enabled = True 
          bet_ok2.draw_button() 
    
    # if Player 2 clicks ok, the play-button gets active. 
    if click_bet_ok2: 
      window.fill((casino_green1), rect=(380,300, 200,50)) 
      player2.color = dark_grey
      player2.draw_text('topleft', 50, 300)
      play.enabled = True 
      bet_ok2.enabled = False 
      bet_ok2.draw_button() 
      active_betRect2 = False


# SET THE GAME WINDOW
  # Start with the window when clicked on 'play' in the bet screen. Set the 2-player-screen. 
  # The 2-player-part will be overwritten with the backgroundcolor when it's a 1-playergame (see further)
  if click_play: 
    # set a new screen 
    window.fill((casino_green1))
    # draw a line in the middle 
    pygame.draw.line(window, yellow_gold, (0, 350), (800, 350), 2)
    # set the title, text and buttons 
    gametitle.draw_text('center', window_width/2, 25)
    player1.color = dark_red
    player1.draw_text('topleft', 20, 60)
    hit1.draw_button()
    stand1.draw_button()
    split1.draw_button()
    player2.color = dark_red
    player2.draw_text('topleft', 400, 60)
    hit2.draw_button()
    stand2.draw_button()
    split2.draw_button()
    dealer.color = dark_red
    dealer.draw_text('topleft', 20, 370)
    yourbet1.draw_text('topleft', 20, 320)
    yourbet2.draw_text('topleft', 400, 320)

    # The bet of the player's is put on the screen with an f-string. 
    # Object of class GameText is created here, because the variable betinput_player must be filled by the player(s).
    bet_player1 = GameText(f'{betinput_player1}€.', font_size2, dark_red) 
    bet_player2 = GameText(f'{betinput_player2}€.', font_size2, dark_red)
    bet_player1.draw_text('topleft', 310, 320)
    bet_player2.draw_text('topleft', 690, 320)

    # screen left bottom: information about round, scores 
    round.draw_text('topleft', 400, 370)
    score.draw_text('topleft', 400, 400)
    player1.color = dark_grey
    player1.draw_text('topleft', 420, 425)
    player2.color = dark_grey 
    player2.draw_text('topleft', 420, 455)
    dealer.color = dark_grey
    dealer.draw_text('topleft', 420, 485)

    if oneplayergame: 
      window.fill((casino_green1), rect=(400,0, 400,345)) 
      window.fill((casino_green1), rect=(420, 455, 90,25))
      hit2.enabled = False 
      stand2.enabled = False
      split2.enabled = False 

  pygame.display.update()

pygame.quit()