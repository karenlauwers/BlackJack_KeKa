import pygame, sys 

# IMPORT ALL FILES THAT CONTRIBUTE TO THE GAME LOOP AND THE WINDOW SETTINGS
from constants import *
from buttons import *
from user_input import * 
from gametext import * 
from deck_and_calculate_Ke import * 

# INITIALISE PYGAME
pygame.init() 

# SET THE PLAYING FIELD
pygame.display.set_caption("BlackJack")

# AID VARIABLES. To help set the game loop and window settings. 
running = True
active_betRect = False  # hulpvariabele om na te gaan of player in de bet rectangle staat. Doel: om een bet te kunnen schrijven in de betRect moet je in die rectangle staat (en er op klikt). Het is niet nodig om te verwijzen naar speler 1 of speler 2 want je kan de variabele voor beiden inzetten. Denk ik.
click_bet_ok = False 
click_play = False 
click_initial_deal = False 
# show_dealer_card = False
click_hit = False 
click_stand = False
# blackjack = False
# blackjack_tie = False 
clicks_on_hit = 0
score = 0 
click_play_again = False 
game_finished = False 
click_split = False

#--END OF AID VARIABLES-- 
#==================================================================================================================
#==================================================================================================================
# GAME LOOP 
while running:
  clock.tick(fps)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN and quit_button.check_click(): 
        running = False

  # EVENT IN BET WINDOW. Player clicks on bet-rectangle and will be able to input bet. 
    if event.type == pygame.MOUSEBUTTONDOWN: 
      if betinput_playerRect.collidepoint(event.pos): 
        active_betRect = True
      else: 
        active_betRect = False

    # EVENT IN BET WINDOW. Player inputs bet; player can only use numbers and backspace to return and delete charachters
    if active_betRect == True: 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # define use of the backspace 
          betinput_player = betinput_player[:-1] 
        elif betinput_player[:1] == '0':  # input cannot start with 0
          betinput_player = betinput_player[:-1]           
        elif event.key in valid_keys and len(betinput_player)<3: #valid_keys is defined in bet.py = only number-keys
          betinput_player += event.unicode

    # EVENT IN BET WINDOW. Player clicks ok to confirm the bet he made.
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok.check_click():
      click_bet_ok = True 
 
    # EVENT IN BET WINDOW. Player clicks on button 'play' in the bet-screen.
    if event.type == pygame.MOUSEBUTTONDOWN and play.check_click(): 
      click_play = True 

    # EVENT IN THE GAME WINDOW. Player clicks on button 'deal cards'.
    if event.type == pygame.MOUSEBUTTONDOWN and initial_deal_button.check_click(): 
      click_initial_deal = True 

    if event.type == pygame.MOUSEBUTTONDOWN and hit.check_click(): 
      click_hit = True 
  
    # EVENT IN THE GAME WINDOW. Player clicks on button 'stand'.
    if event.type == pygame.MOUSEBUTTONDOWN and stand.check_click():
      click_stand = True
      show_dealer_card = True 

    # EVENT IN THE GAME WINDOW. Player clicks on button 'play again'.
    if event.type == pygame.MOUSEBUTTONDOWN and play_again.check_click():
      click_play_again = True
    
    # EVENT IN THE GAME WINDOW. Player clicks on button 'split'.
    if event.type == pygame.MOUSEBUTTONDOWN and split.check_click():
      click_split = True

#--END OF EVENTS-- 
#===============================================================================================================
#===============================================================================================================
# GAME DESIGN. SETTING (DRAWING AND BLITTING) THE WINDOWS 
  # SET THE MAIN WINDOW. Fill with colour 
      
#----------------------------------------------------------------------------------------------------------------
# EVENTUEEL IN TE VOEGEN # SET THE ASK-FOR-NAME WINDOW

#----------------------------------------------------------------------------------------------------------------
  # SET THE BET WINDOW.
  # Set text and buttons 
  # Start by setting the screen
  window.fill((casino_green1))
  bet_title.draw_text('center', window_width/2, 70) 
  disclaimer.draw_text('center', window_width/2, 120)
  explanation.draw_text('center', window_width/2, 140)
  player_text.draw_text('center',window_width/2, 180)
  bet_ok.draw_button()
  play.draw_button()
  quit_button.draw_button() 

  # Draw the textboxes in which the players are going to put their bet. 
  # The color of the box is red when the box is active and can be modified; grey when it isn't. 
  # First define the colors 
  if active_betRect: 
      color = color_active
  else: 
      color = color_passive
  
  # Then draw the textboxes
  pygame.draw.rect(window, color, betinput_playerRect, 2, 5)
  bet_surface = font_size2.render(betinput_player, True, white)
  window.blit(bet_surface, (betinput_playerRect.x+5, betinput_playerRect.y+3))

  # BET WINDOW FOR 1PLAYERGAME
  # Setings for the play-button: you can only click play if you entered a bet between 1 and 999.
  if betinput_player =='0' or len(betinput_player)<1: 
    bet_ok.enabled = False
    bet_ok.draw_button()
  else: 
    bet_ok.enabled = True
    bet_ok.draw_button() 
    
  if click_bet_ok: 
    play.enabled = True 
    bet_ok.enabled = False
   
#----------------------------------------------------------------------------------------------------------------
# SET THE GAME WINDOW
  # Start with the window when clicked on 'play' in the bet screen. 
  if click_play: 
    # set a new screen 
    window.fill((casino_green1))
    # draw a line in the middle 
    pygame.draw.line(window, yellow_gold, (0, 340), (800, 340), 2)
    # set the title, text and buttons 
    gametitle.draw_text('center', window_width/2, 25)
    player_text.color = dark_red
    player_text.draw_text('center', window_width/2, 60)
    hit.draw_button()
    stand.draw_button()
    split.draw_button()
    double.draw_button()
    dealer_text.color = dark_red
    dealer_text.draw_text('center', window_width/2, 360)
    initial_deal_button.draw_button()
    quit_button.draw_button() 

    # The bet of the player's is put on the screen with an f-string. 
    # Object of class GameText is created here, because the variable betinput_player must be filled by the player(s).
    bet_player = GameText(f'Bet     {betinput_player}€', font_size1, dark_grey) 
    bet_player.draw_text('topleft', 100, 120)
    bet_player.draw_text('topleft', 635, 120)
    hand_value_player = GameText(f'Value  {player.value}', font_size1, dark_grey) 
    hand_value_player.draw_text('topleft', 100, 140)   
    hand_value_player.draw_text('topleft', 635, 140)  # only to show where the text will be drawn if split hand
    if show_dealer_card == True:    
      hand_value_dealer = GameText(f'Value {dealer.value}', font_size1, dark_grey) 
      hand_value_dealer.draw_text('topleft', 360, 420) 

    # Draw the cards on the screen 
    hand_text.draw_text('topleft', 100, 160)
    split_hand_text.draw_text('topleft', 635, 160)
    player.draw_card(0, 100, 190)
    player.draw_card(1, 120, 190)
    if len(player.card_img) > 2:   
      player.draw_card(2, 200, 190)
    if len(player.card_img) > 3: 
      player.draw_card(3, 280, 190)
    if split_hand(player_hand2, deck):
      player_hand2.draw_card(0, 450,190)  # only to show where the split hand cards will be drawn 
      player_hand2.draw_card(0, 470, 190) # only to show where the split hand cards will be drawn 
      player_hand2.draw_card(0, 550, 190) # only to show where the split hand cards will be drawn 
      player_hand2.draw_card(0, 630, 190) # only to show where the split hand cards will be drawn 
    dealer.draw_card(0, 270, 450)
    if show_dealer_card == False : 
      dealer.hide_card(290, 450)
    else: 
      dealer.draw_card(1, 290, 450)
    if len(dealer.card_img) > 2:
      dealer.draw_card(2, 370, 450)
    if len(dealer.card_img) > 3: 
      dealer.draw_card(3, 450, 450)

# result text on the screen
    if blackjack: 
      blackjack_text.draw_text('topleft', 100, 300)
      score = int(betinput_player) + (int(betinput_player)*1.5)
      show_dealer_card = True 
      game_finished = True
    if blackjack_tie: 
      tie_text.draw_text('topleft', 100, 300)
      score = int(betinput_player) 
      show_dealer_card = True 
      game_finished = True
    if tie: 
      tie_text.draw_text('topleft', 100, 300)  
      score = int(betinput_player) 
      show_dealer_card = True    
      game_finished = True
    if win:
      win_text.draw_text('topleft', 100, 300)  
      score = int(betinput_player) + (int(betinput_player)*1)
      game_finished = True
    if lose:
      lose_text.draw_text('topleft', 100, 300)  
      score = 0
      show_dealer_card = True 
      game_finished = True
    if busted_player: 
      busted_text.draw_text('topleft', 100, 300)  
      score = 0
      show_dealer_card = True 
      game_finished = True
   
    # Set information on the right bottom of the screen: information about actual round (nog niet klaar), scores (nog niert klaar)
    round_text.draw_text('topleft', 20, 480)
    score_text = GameText(f'Score   {score}', font_size2, white)
    score_text.draw_text('topleft', 20, 520)
    play_again.draw_button()

#--END OF WINDOW SETTING-- 
#=================================================================================================================
#=================================================================================================================
# THE GAME 
  # INITIAL DEAL: 
    if click_initial_deal == True: # becomes True by clicking on the button "deal cards", zie event loop
      hit.enabled = True 
      stand.enabled = True
      split.enabled = True
      initial_deal_player()
      initial_deal_dealer()
      if player.value == 21: 
        if dealer.value == 21: 
          blackjack_tie = True
        elif dealer.value != 21: 
          blackjack = True
        
    click_initial_deal = False   

    if len(player.cards) == 2: 
      initial_deal_button.enabled = False
      initial_deal_button.draw_button()
    
  # if player clicks hit 
    if click_hit == True: 
      clicks_on_hit += 1
      hit_card()
      print('player card_img', player.card_img)
      print(dealer.value)
      if player.value > 21:
        busted_player = True
      if clicks_on_hit == 2: 
        hit.enabled = False 
        hit.draw_button()
        stand.enabled = False 
        stand_action()
        if player.value > 21:
          busted_player = True
        if dealer.value > 21: 
          busted_dealer = True 
          win = True 
        if player.value > dealer.value: 
            win = True 
        elif player.value == dealer.value: 
            tie = True                        
        elif player.value < dealer.value: 
            lose = True 

    click_hit = False 
       
    if click_stand == True:  
      stand.enabled = False 
      stand_action() 
      if player.value > 21:
        busted_player = True
      if dealer.value > 21: 
        busted_dealer = True 
        win = True 
      else: 
        if player.value > dealer.value: 
          win = True 
        if player.value == dealer.value: 
          tie = True                        
        if player.value < dealer.value: 
          lose = True 

    click_stand = False 

    if click_split == True:
      split.enabled = False
      split_hand(player_hand2, deck)
    
    click_split = False

    if click_play_again == True:
      player = Hand()
      dealer = Hand()
      deck.shuffle()
      active_betRect = False
      click_bet_ok = False 
      click_play = False
      click_initial_deal = False 
      click_hit = False 
      click_stand = False
      clicks_on_hit = 0
      score = 0 
      game_finished = False
    
    click_play_again == False
    # Keert terug naar bet screen, maar wanneer op play wordt geklikt ==> spel wordt niet gestart?

  pygame.display.update()
pygame.quit()