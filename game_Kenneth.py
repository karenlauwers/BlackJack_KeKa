import pygame, sys 

# IMPORT ALL FILES THAT CONTRIBUTE TO THE GAME LOOP AND THE WINDOW SETTINGS
from constants import *
from buttons import *
from user_input import * 
from gametext import * 
from calculate_updateKa import * 
from blackjack_deck_updateKa import *

# INITIALISE PYGAME
pygame.init() 

# SET THE PLAYING FIELD
pygame.display.set_caption("BlackJack")

# AID VARIABLES. To help set the game loop and window settings. 
running = True
click_button_1player = False  # hulpvariabele om na te gaan of de button_1player geklikt wordt.
click_button_2player = False 
oneplayergame = False
twoplayergame = False 
active_betRect1 = False  # hulpvariabele om na te gaan of player in de bet rectangle staat. Doel: om een bet te kunnen schrijven in de betRect moet je in die rectangle staat (en er op klikt). Het is niet nodig om te verwijzen naar speler 1 of speler 2 want je kan de variabele voor beiden inzetten. Denk ik.
active_betRect2 = False 
click_bet_ok1 = False 
click_bet_ok2 = False 
click_play = False 
click_initial_deal = False 
click_hit1 = False
click_hit2 = False
click_stand1 = False
click_stand2 = False

#--END OF AID VARIABLES-- 
#==================================================================================================================
#==================================================================================================================
# GAME LOOP 
while running:
  # clock.tick(fps)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN and quit_button.check_click(): 
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
      
    # EVENT IN BET WINDOW. Player clicks ok to confirm the bet he made.
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok1.check_click():
      click_bet_ok1 = True 
    
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok2.check_click():
      click_bet_ok2 = True 

    # EVENT IN BET WINDOW. Player clicks on button 'play' in the bet-screen.
    if event.type == pygame.MOUSEBUTTONDOWN and play.check_click(): 
      click_play = True 

    # EVENT IN THE GAME WINDOW. Player clicks on button 'deal cards'.
    if event.type == pygame.MOUSEBUTTONDOWN and initial_deal.check_click(): 
      click_initial_deal = True 

    # EVENT IN THE GAME WINDOW. Player clicks on button 'hit' to get one more card.
    if event.type == pygame.MOUSEBUTTONDOWN and hit1.check_click():
      click_hit1 = True

    if event.type == pygame.MOUSEBUTTONDOWN and hit2.check_click():
      click_hit2 = True

    # EVENT IN THE GAME WINDOW. Player clicks on button 'stand'.
    if event.type == pygame.MOUSEBUTTONDOWN and stand1.check_click():
      click_stand1 = True

    if event.type == pygame.MOUSEBUTTONDOWN and stand2.check_click():
      click_stand2 = True

    # AF TE WERKEN 
    # EVENT IN THE GAME WINDOW. Player1 clicks 'hit' to get one more card. 
    # if event.type == pygame.MOUSEBUTTONDOWN and hit1.check_click(): 
      # click_hit1 = True 
      # en deze variabele kan in THE GAME gebruikt worden om de functie 'hit_card(player)' op te roepen voor de player die je definieert, in dit geval 'hit_card(player1)

    #OPMERKING
    # Als we SPLIT toepassen, dan is het niet voldoende om enkel voor player1 en player2 een instance van de class Hand te maken. 
    # Want dan kan elke speler 2 handen hebben. Ik stel voor dat we het aantal splits beperken tot 1. Dus dan kan elke speler 2 handen hebben.
    # Dus we zullen in de calculate-file (we verwijzen nu naar de calculate-update file) de variabelen player1 en player moeten hernoemen naar
    # 'player1_hand1' en 'player1_hand2'enz. Ik weet nog niet precies hoe, maar als we met split willen werken dan moet dit aangepast worden. 
      
#--END OF EVENTS-- 
#===============================================================================================================
#===============================================================================================================
# GAME DESIGN. SETTING (DRAWING AND BLITTING) THE WINDOWS 
  # SET THE MAIN WINDOW. Fill with colour 
  window.fill((casino_green1))

#----------------------------------------------------------------------------------------------------------------
  # SET THE WELCOME WINDOW. With choice 1 or 2playergame
  welcome.draw_text('center', window_width/2, 90)
  button_1player.draw_button()
  button_2player.draw_button()
  quit_button.draw_button() 

#----------------------------------------------------------------------------------------------------------------
  # EVENTUEEL IN TE VOEGEN # SET THE ASK-FOR-NAME WINDOW

#----------------------------------------------------------------------------------------------------------------
  # SET THE BET WINDOW.
  # Set text and buttons 
  # Start by setting the screen for 1- and 2-player game 
  if click_button_1player or click_button_2player : 
    window.fill((casino_green1))
    bet_title.draw_text('center', window_width/2, 70) 
    disclaimer.draw_text('center', window_width/2, 120)
    explanation.draw_text('center', window_width/2, 140)
    player1_text.draw_text('topleft',50, 180)
    bet_ok1.draw_button()
    player2_text.draw_text('topleft', 50, 290)
    bet_ok2.draw_button()
    play.draw_button()
    quit_button.draw_button() 

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
    window.blit(bet_surface, (betinput_player1Rect.x+5, betinput_player1Rect.y+3))

    pygame.draw.rect(window, color2, betinput_player2Rect, 2, 5)
    bet_surface = font_size2.render(betinput_player2, True, white)
    window.blit(bet_surface, (betinput_player2Rect.x+5, betinput_player2Rect.y+1))
  
    if click_button_1player: 
      oneplayergame = True 
      twoplayergame = False 

    elif click_button_2player: 
      oneplayergame = False 
      twoplayergame = True 

  # BET WINDOW FOR 1PLAYERGAME
    if oneplayergame: 
      # for 1playergame: hide the player2-part by partly filling the screen. 
      window.fill((casino_green1), rect=(0,270, 400,120)) 
      # Disable the buttons of the previous screen (welcome window with 1- or 2playergamebuttons). 
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
    
    # If player 1 has clicked ok, the 'please bet'-text moves to player 2 and the color 
    if click_bet_ok1: 
      betplease.draw_text('topleft', 380, 290)
      window.fill((casino_green1), rect=(380,180,190,50)) 
      player1_text.color = dark_grey
      player1_text.draw_text('topleft', 50, 180)
      player2_text.color = dark_red
      player2_text.draw_text('topleft', 50, 290)
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
    
    # if Player 2 clicks ok, the play-button gets active, ok-button and the inputbox get inactive 
    if click_bet_ok2: 
      window.fill((casino_green1), rect=(380,290, 200,50)) 
      player2_text.color = dark_grey
      player2_text.draw_text('topleft', 50, 290)
      bet_ok2.enabled = False 
      bet_ok2.draw_button() 
      play.enabled = True 
      active_betRect2 = False

#----------------------------------------------------------------------------------------------------------------
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
    player1_text.color = dark_red
    player1_text.draw_text('topleft', 20, 50)
    hit1.draw_button()
    stand1.draw_button()
    split1.draw_button()
    double1.draw_button()
    player2_text.color = dark_red
    player2_text.draw_text('topleft', 400, 50)
    hit2.draw_button()
    stand2.draw_button()
    split2.draw_button()
    double2.draw_button()
    dealer_text.color = dark_red
    dealer_text.draw_text('topleft', 20, 360)
    bet.draw_text('topleft', 20, 317)
    bet.draw_text('topleft', 400, 317)
    hand_value.draw_text('topleft', 20, 290)
    hand_value.draw_text('topleft', 400, 290)
    initial_deal.draw_button()
    quit_button.draw_button() 

    # The bet of the player's is put on the screen with an f-string. 
    # Object of class GameText is created here, because the variable betinput_player must be filled by the player(s).
    bet_player1 = GameText(f'{betinput_player1}€', font_size2, dark_red) 
    bet_player2 = GameText(f'{betinput_player2}€', font_size2, dark_red)
    bet_player1.draw_text('topleft', 100, 317)
    bet_player2.draw_text('topleft', 480, 317)
    hand_value_player1 = GameText(f'{player1.value}', font_size2, dark_red) 
    hand_value_player1.draw_text('topleft', 100, 290)   
    hand_value_player2 = GameText(f'{player2.value}', font_size2, dark_red) 
    hand_value_player2.draw_text('topleft', 480, 290)    

    # Set information on the right bottom of the screen: information about actual round (nog niet klaar), scores (nog niert klaar)
    round.draw_text('topleft', 400, 360)
    score.draw_text('topleft', 400, 400)
    player1_text.color = dark_grey
    player1_text.draw_text('topleft', 420, 435)
    player2_text.color = dark_grey 
    player2_text.draw_text('topleft', 420, 465)
    dealer_text.color = dark_grey
    dealer_text.draw_text('topleft', 420, 495)

    if oneplayergame: 
        window.fill((casino_green1), rect=(400,45, 400,305)) 
        window.fill((casino_green1), rect=(420, 470, 90,31))
        hit2.enabled = False 
        stand2.enabled = False
        split2.enabled = False 

#--END OF WINDOW SETTING-- 
#=================================================================================================================
#=================================================================================================================
# THE GAME 
  # INITIAL DEAL: 
  # The print-functies zijn niet bedoeld voor het spel, maar om te zien wat er gebeurt. 
  # Want er zitten nog geen beelden in het spel, waardoor je op het scherm nog niet ziet wat er bedeeld wordt. 
  # De hand_value wordt wel berekend, ook al staat het hogerop (zie lijn 256-259)
    if click_initial_deal == True: # becomes True by clicking on the button "deal cards", zie event loop
      # initial_deal.enabled = True
      # initial_deal.draw_button()
      if twoplayergame: 
        initial_deal_twoplayergame()
        player1.get_filename()
        player1.draw_card()
        player2.get_filename()
        player2.draw_card()
        dealer.get_filename()
        dealer.draw_card()
        dealer.hide_card()
        player1.calculate_hand()
        player2.calculate_hand()
        print(player1.cards)
        print(player2.cards)
        print(dealer.cards)
        print(player1.value)
    
      if oneplayergame: 
        initial_deal_oneplayergame()
        player1.get_filename()
        player1.draw_card()
        dealer.get_filename()
        dealer.draw_card()
        dealer.hide_card()
        player1.calculate_hand()
        print(player1.cards)
        print(dealer.cards)
        print(player1.value)
        
    click_initial_deal = False   

    if len(player1.cards) == 2: 
      initial_deal.enabled = False
      initial_deal.draw_button()

    # HIT: je kan op hit duwen en 1 kaart wordt getrokken.
    # Print functies staan er terug bij voor verduidelijking
    if click_hit1:
      hit_card(player1)
      player1.get_filename()
      player1.draw_card()
      player1.calculate_hand()
      print(player1.cards)
      print(player1.value)
      print(hit_card(player1))
      click_hit1 = False

    if player1.value > 21:
      hit1.enabled = False
      hit1.draw_button()
      stand1.enabled = False

    if click_hit2:
      hit_card(player2)
      player2.get_filename()
      player2.draw_card()
      player2.calculate_hand()
      click_hit2 = False

    if player2.value > 21:
      hit2.enabled = False
      hit2.draw_button()
      stand2.enabled = False

    # STAND:
    if click_stand1:
      print(f"Player1 stands with cards: {player1.cards} and value: {player1.value}")
      stand_action(player1, player2, dealer, deck)
      print(stand_action(player1, player2, dealer, deck))
      click_stand1 = False
      hit1.enabled = False
      hit1.draw_button()
      stand1.enabled = False
      stand1.draw_button()
      
    if click_stand2:
      print(f"Player2 stands with cards: {player2.cards} and value: {player2.value}")
      stand_action(player1, player2, dealer, deck)
      print(stand_action(player1, player2, dealer, deck))
      click_stand2 = False
      hit2.enabled = False
      hit2.draw_button()
      stand2.enabled = False
      stand2.draw_button()
      
    # Dealer blijft 1 kaart trekken ondanks >= 17??
    # Two player game wordt resultaat meteen beslist vooraleer het aan de volgende speler is .... 
    # Hoe maak je dit turn based?
    # Hoe resultaten met text in game window krijgen(player wins, dealer wins....?)
    # Hoe kaarten op scherm krijgen?
    # SPLIT ?

  pygame.display.update()
pygame.quit()      