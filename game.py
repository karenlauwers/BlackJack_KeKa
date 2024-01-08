# Acknowledgments:
# Thanks to Bobinson's public repository on GitHub - we used the card images of this repository. 
# Thanks to Mozes721's public repository on GitHub - from which we learned more about the structure of the game.
# Thanks to LeMaster Tech and Code Coach for inspiration on the game.
import pygame

# IMPORT ALL FILES THAT CONTRIBUTE TO THE GAME LOOP AND THE WINDOW SETTINGS
from constants import *
from buttons import *
from user_input import * 
from gametext import * 
from deck_and_calculate import * 

# INITIALISE PYGAME
pygame.init() 

# SET THE PLAYING FIELD
pygame.display.set_caption("BlackJack")

# AID VARIABLES. To help set the game loop and window settings. 
running = True

# To verify if the player is in the rectangle. To make the inputbox for name/bet ready for input.
active_nameRect = False 
active_betRect = False  

# To check if the button is clicked. Aid variables introduced in the game loop. 
click_start_game = False 
click_bet_ok = False 
click_play = False 
click_deal = False 
click_hit = False 
click_stand = False
click_next_round = False 

# To check the number of times the button 'hit' is clicked
clicks_on_hit = 0

# To control whether to hide or to show the second dealer card 
show_dealer_card = False

# To control the drawing of the results/gametext on the screen 
blackjack = False
blackjack_tie = False 
win = False
lose = False 
tie = False

# Score to be calculated after having defined the result. Starts at 0.
score = 0 

# To control the calculation of the score. To make sure the score is only calculated once at the end of a round.
blackjack_scorefixer = False
tie_scorefixer = False 
win_scorefixer = False 
lose_scorefixer = False
busted_player = False 

# To control the timing of the drawing of the final text on the screen at the end of the 5the round
wait_a_second = False 
wait_a_second_stopper = False 

# To keep track of the round that the player is playing
round = 1

# To control start and end of the rounds to be played and to control the end of the game 
game_finished = False 
round_finished = False 

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

  # EVENTS IN START WINDOW. 
    # Player clicks on name-rectangle and will be able to input name. 
    if event.type == pygame.MOUSEBUTTONDOWN:
      if nameinput_playerRect.collidepoint(event.pos): 
        active_nameRect = True  

    # After clicking on the name-rectangle, player can input name. 
    if active_nameRect: 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # Define use of the backspace 
          nameinput_player = nameinput_player[:-1] 
        elif event.key and len(nameinput_player)<20: # Input can be any key, max. 19 tekens
          nameinput_player += event.unicode 

    # If the name is put in, player clicks button 'start game'
    if event.type == pygame.MOUSEBUTTONDOWN and start_game.check_click(): 
      click_start_game = True  

  # EVENTS IN BET WINDOW.
    # Idem name-rectangle. Player clicks rectangle and will be able to input bet. 
    if event.type == pygame.MOUSEBUTTONDOWN:
      if betinput_playerRect.collidepoint(event.pos): 
        active_betRect = True
      
    # After clicking on the bet-rectangle, player can input bet. 
    if active_betRect == True: 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # Define use of the backspace 
          betinput_player = betinput_player[:-1] 
        elif betinput_player[:1] == '0':  # Input cannot start with 0
          betinput_player = betinput_player[:-1]           
        elif event.key in valid_keys and len(betinput_player)<3: #'valid_keys' is defined in user_input.py = only number-keys
          betinput_player += event.unicode 

    # Player clicks ok to confirm the bet he made.
    if event.type == pygame.MOUSEBUTTONDOWN and bet_ok.check_click():
      click_bet_ok = True 
 
    # Player clicks on button 'play' in the bet-screen.
    if event.type == pygame.MOUSEBUTTONDOWN and play.check_click(): 
      click_play = True 

  # EVENTS IN THE GAME WINDOW. 
    # Player clicks on button 'deal cards'.
    if event.type == pygame.MOUSEBUTTONDOWN and deal_button.check_click(): 
      click_deal = True 

    # Player clicks on button 'hit'
    if event.type == pygame.MOUSEBUTTONDOWN and hit.check_click(): 
      click_hit = True 
  
    # Player clicks on button 'stand'.
    if event.type == pygame.MOUSEBUTTONDOWN and stand.check_click():
      click_stand = True

    # Player clicks on button 'next round'
    if event.type == pygame.MOUSEBUTTONDOWN and next_round.check_click():
      click_next_round = True 

    # Time delay of 2 sec between end of 5th (last) round and the final text on the screen. 
    # To make sure you can read the result of the last round before your final score is printed. 
    if wait_a_second: 
      pygame.time.delay(2000) 
      # To control the time delay and to make sure it only runs once 
      wait_a_second_stopper = True
 
#--END OF EVENTS-- 
#===============================================================================================================
#===============================================================================================================
# WELCOME WINDOW. NAME INPUT.
  # Set the welcome window, gametexts and buttons.
  window.fill((casino_green1)) 
  welcome.draw_text('center', window_width/2, 70) 
  gametitle.draw_text('center', window_width/2, 110)
  name_question.draw_text('center', window_width/2, 170)
  name_explanation.draw_text('center', window_width/2, 200)
  start_game.draw_button()
  quit_button.draw_button() 

  # Inputbox for name 
  # The color of the box is red when the box is active and can be modified; grey when it isn't. 
    # First define the colors 
  if active_nameRect: 
    color = color_active
  else: 
    color = color_passive
  
    # Then draw the textboxes
  pygame.draw.rect(window, color, nameinput_playerRect, 2, 5)
  name_surface = font_size2.render(nameinput_player, True, white)
  window.blit(name_surface, (nameinput_playerRect.x+5, nameinput_playerRect.y+3))
  nameinput_playerRect.w = max(140, name_surface.get_width() + 10) # to make the inputbox wider if you need more characters than set by the box. 
  
  # Setings for the play-button: you can only click 'start game' if you entered at least 1 character.
  if len(nameinput_player)<1: 
    start_game.enabled = False
    start_game.draw_button()
  else: 
    start_game.enabled = True
    start_game.draw_button()       

# BET WINDOW. BET INPUT. 
  # Set the bet window after having clicked 'start game'. 
  # Fill with color, set gametexts, draw buttons. 
  if click_start_game: 
    active_nameRect = False 
    window.fill((casino_green1))
    bet_title.draw_text('center', window_width/2, 70) 
    disclaimer.draw_text('center', window_width/2, 120)
    explanation.draw_text('center', window_width/2, 140)
    betplease = GameText(f'Your bet, please, {nameinput_player}', font_size2, dark_red)
    betplease.draw_text('center',window_width/2, 180)
    bet_ok.draw_button()
    play.draw_button()
    quit_button.draw_button() 
    start_game.enabled = False 

  # Draw the inputbox in which the player is going to put his bet. 
  # The color of the box is red when the box is active and can be modified; grey when it isn't. 
    # First define the colors 
    if active_betRect: 
      color = color_active
    else: 
      color = color_passive
  
    # Then draw the inputbox
    pygame.draw.rect(window, color, betinput_playerRect, 2, 5)
    bet_surface = font_size2.render(betinput_player, True, white)
    window.blit(bet_surface, (betinput_playerRect.x+5, betinput_playerRect.y+3))

    # Settings for the play-button: you can only click play if you entered a bet between 1 and 999.
    if betinput_player =='0' or len(betinput_player)<1: 
      bet_ok.enabled = False
      bet_ok.draw_button()
    else: 
      bet_ok.enabled = True
      bet_ok.draw_button() 
    
    # If you click ok to confirm your bet, the play-button is enabled 
    if click_bet_ok: 
      bet_ok.enabled = False
      bet_ok.draw_button() 
      play.enabled = True     

#--END OF INPUT WINDOWS --  
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# GAME WINDOW SETTINGS. CARDS, TEXTS, BUTTONS.
  # Game window is set when clicked 'play'.  
  # If there is GameText to display that requires input from the player (name, bet) (f-string), 
  # the GameText is created here and not in the file gametext.py. 
  # Because, if not, the variable doesn't take the input created by the user but stays empty.
  if click_play: 
    # Set a new screen 
    # Set a new screen 
    window.fill((casino_green1))
    # Draw a line in the middle 
    # Draw a line in the middle 
    pygame.draw.line(window, yellow_gold, (0, 340), (800, 340), 2)
    # Set title, gametexts and buttons 
    gametitle.draw_text('center', window_width/2, 25)
    playername = GameText(f'{nameinput_player}', font_size2, dark_red)
    playername.draw_text('center', window_width/2, 60)
    hit.draw_button()
    stand.draw_button()
    dealer_text.color = dark_red
    dealer_text.draw_text('center', window_width/2, 360)
    deal_button.draw_button()
    next_round.draw_button()
    quit_button.draw_button() 

    # Set information on the screen:
    # The bet of the player and the value of the cards on the window. 
    bet_player = GameText(f'Bet     {betinput_player}€', font_size1, dark_grey) 
    bet_player.draw_text('topleft', 370, 120)
    hand_value_player = GameText(f'Value  {player.value}', font_size1, dark_grey) 
    hand_value_player.draw_text('topleft', 370, 140)   

    # Information about actual round and score 
    round_text = GameText(f'Round  {round} of 5', font_size2, white) 
    round_text.draw_text('topleft', 20, 480)
    score_text = GameText(f'Score   {score}€', font_size2, white)
    score_text.draw_text('topleft', 20, 520)  

    # Prepare the end of a round 
    if blackjack or blackjack_tie or busted_player or tie or win or lose:
      show_dealer_card = True # to make sure the 2nd dealer card will be shown
      hit.enabled = False # to disable hit button at the end of the round, if there is a result 
      hit.draw_button()
      stand.enabled = False # idem for stand button 
      stand.draw_button() 
      if round < 5: # to play a maximum of 5 rounds 
        round_finished = True 
      if round == 5: # to prepare for the time delay between the end of the 5th round and the final text
        wait_a_second = True 
      # Set the result on the screen, at the end of a round
      if blackjack: 
        blackjack_text.draw_text('center', window_width/2, 310) 
      if blackjack_tie or tie: 
        tie_text.draw_text('center', window_width/2, 310)
      if win:
        win_text.draw_text('center', window_width/2, 310) 
      if lose:
        lose_text.draw_text('center', window_width/2, 310)  
      if busted_player: 
        busted_text.draw_text('center', window_width/2, 310)  
      # During 5 rounds, the score falls back to the score of the previous round 
      # To make this work, their is another variable needed: scorefixer, a boolean that will be true if there's a result and False if the score is set. 
      # You need another variable for this than 'blackjack', 'win' etc. Else, the result-text will only appear shortly on the screen because of the loop.
      if betinput_player != '': 
        if blackjack_scorefixer: 
          score += int(betinput_player) + (float(betinput_player)*1.5)
          blackjack_scorefixer = False
        if tie_scorefixer: 
          score += int(betinput_player) 
          tie_scorefixer = False 
        if win_scorefixer:
          score += int(betinput_player) + (int(betinput_player)*1)
          win_scorefixer = False 
        if lose_scorefixer:
          score += 0
          lose_scorefixer = False 

    # Draw the cards on the screen - see draw-function in file deck_and_calculate line 69
    # Draw the player's cards 
    if len(player.card_img) > 1: # draw the first 2 cards (index 0 and 1)
      player.draw_card(0, 270, 180)
      player.draw_card(1, 290, 180)
    if len(player.card_img) > 2:   # draw the 3th card, if there is a 3th card (and/or 4th) card in the list (index 2)
      player.draw_card(2, 370, 180)
    if len(player.card_img) == 4: 
      player.draw_card(3, 450, 180) # draw the 4th card, if there is a 4th card in the list (index 3)
    
    # Draw the dealer's cards 
    dealer.draw_card(0, 270, 450) # draw the first card of the dealer 
    if show_dealer_card == False and len(dealer.card_img) > 1: 
      # Hide the second card of the dealer - only draw this image if there is more than 1 card in the list. 
      # If not, the image is immediately drawn on the screen when you enter the game window. 
      dealer.hide_card(290, 450)
    elif show_dealer_card and len(dealer.card_img) > 1: 
      # Draw the 2nd dealer card if the variable show_dealer_card is active (at the end of the round)
      dealer.draw_card(1, 290, 450)
    if len(dealer.card_img) > 2:
      dealer.draw_card(2, 370, 450)
    if len(dealer.card_img) == 4: 
      dealer.draw_card(3, 450, 450)
    if show_dealer_card == True: # the dealer's value is printed on the screen at the end of the round 
      hand_value_dealer = GameText(f'Value {dealer.value}', font_size1, dark_grey) 
      hand_value_dealer.draw_text('topleft', 360, 420) 

    # End text on the screen after 5 rounds (and after a time delay of 2 seconds)
    if game_finished: 
      window.fill(casino_green1, (150,80,500,650))
      end_of_game = GameText('Thanks for playing BlackJack with us.', font_size3, yellow_gold)
      end_of_game.draw_text('center', window_width/2, 160)
      your_total_bet_was = GameText(f'Your total bet was 5 x {betinput_player}€: {5*float(betinput_player)}€.', font_size2, black)
      your_total_bet_was.draw_text('center', window_width/2, 200) 
      your_final_score_is = GameText(f'Your final score is {score}€.', font_size2, black)
      your_final_score_is.draw_text('center', window_width/2, 230)
      if betinput_player != '': 
        if (5*float(betinput_player)) < score: 
          your_gain = GameText(f'{nameinput_player}, your gain is {score - (5*float(betinput_player))}€!', font_size3, black)
          your_gain.draw_text('center',window_width/2, 270)
        elif (5*float(betinput_player)) == score: 
          break_even = GameText(f'{nameinput_player}, you are break even.', font_size3, black)
          break_even.draw_text('center', window_width/2, 270)
        elif (5*float(betinput_player)) > score: 
          your_loss = GameText(f'{nameinput_player}, your loss is {-(score - (5*float(betinput_player)))}€...', font_size3, black)
          your_loss.draw_text('center', window_width/2, 270)
      see_you_next_time = GameText("See you next time. Click 'quit' to leave.", font_size2, black)
      see_you_next_time.draw_text('center', window_width/2, 310)
            
#--END OF GAME WINDOW SETTING-- 
#=================================================================================================================
#=================================================================================================================
# GAME ACTIONS. 
  # DEAL: 
  if click_deal == True: 
    # If clicked on 'deal cards', hit and stand button become active 
    hit.enabled = True 
    hit.draw_button()
    stand.enabled = True
    stand.draw_button()
    # Deal action: player and dealer get 2 cards - function defined in file 'deck_and_calculate', line 112
    deal_cards() 
    # After dealing the cards, the result is immediately checked for 'blackjack'
    if player.value == 21: 
      if dealer.value == 21: 
        blackjack_tie = True
        tie_scorefixer  = True 
      elif dealer.value != 21: 
        blackjack = True
        blackjack_scorefixer = True

  # End the action to make sure the loop is only ran once during a round. 
  # If not 2 cards to dealer and player will be dealed over and over again until the cards_deck is empty and you get an error. 
  click_deal = False    

  # After dealing the cards, the deal button is disabled. Will only be enabled again if 'next round' is clicked.
  if len(player.cards_hand) == 2: 
    deal_button.enabled = False
    deal_button.draw_button()
    
  # Player asks for one more card
  if click_hit == True: 
    clicks_on_hit += 1 # counts clicks_on_hit to keep track of number of hits and to limit number of hits to 2 (see line 388)
    # Gives one more card to the player. Function defined in file 'deck_and_calculate', line 127.
    hit_card()

    # Check if player is busted 
    if player.value > 21:
      busted_player = True
      lose_scorefixer = True 
      
    # Player can only ask for 2 more cards. After 2 more cards, buttons hit and stand are disabled. 
    if clicks_on_hit == 2: 
      hit.enabled = False 
      hit.draw_button()
      stand.enabled = False 
      stand.draw_button()
      # Dealer takes action: dealer takes one more card until value is 17, with a maximum of two more cards. 
      dealer_action() # Function defined in 'deck_and_calculate' line 137
      # Result is evaluated 
      if player.value > 21:
        busted_player = True
        lose_scorefixer = True 
      elif dealer.value > 21: 
        win = True 
        win_scorefixer = True 
      elif player.value > dealer.value: 
        win = True 
        win_scorefixer = True 
      elif player.value == dealer.value: 
        tie = True   
        tie_scorefixer = True                      
      elif player.value < dealer.value: 
        lose = True  
        lose_scorefixer = True 

 # End the action to make sure the loop is only ran once during a round. 
  click_hit = False 
       
  if click_stand == True:  
    # If player clicks stand button, stand and hit-buttons are disabled. 
    stand.enabled = False 
    stand.draw_button()
    hit.enabled = False 
    hit.draw_button()
    # Dealer takes action:
    dealer_action() 
    # Result is evaluated 
    if player.value > 21:
      busted_player = True
      lose_scorefixer = True 
    elif dealer.value > 21: 
      win = True 
      win_scorefixer = True
    elif player.value > dealer.value: 
      win = True 
      win_scorefixer = True 
    elif player.value == dealer.value: 
      tie = True   
      tie_scorefixer = True                      
    elif player.value < dealer.value: 
      lose = True 
      lose_scorefixer = True 

  # End the action to make sure the loop is only ran once during a round. 
  click_stand = False 

  # End the time delay to make sure it does not keep on running over and over again and blocking the game. 
  if wait_a_second_stopper == True: 
    wait_a_second = False
    game_finished = True 

  # End-of-round settings: at end of round, the next_round button is enabled 
  if round_finished: 
    next_round.enabled = True
    next_round.draw_button()
    # By setting the round_finished-variable to False, the next_round-button is disabled
    # So you cannot click on this button anymore until the round is finished 
    round_finished = False
  
  # End-of-game settings: at the end of the game, the next_round-button is disabled. Only quit-button is still active. 
  if game_finished:
    next_round.enabled = False 
    next_round.draw_button()
 
 # If you click next_round-button, game settings are reset, card deck is reshuffled.
  if click_next_round: 
    round += 1 # keep track of the number of rounds 
    deck.shuffle() # reshuffle the deck 
    deal_button.enabled = True # enable deal-button 
    deal_button.draw_button()
    next_round.enabled = False # disable next_rount-button 
    next_round.draw_button
    del(player.cards_hand[:]) # empty the lists cards_hand and card_img 
    del(player.card_img[:])
    del(dealer.cards_hand[:])
    del(dealer.card_img[:])
    player.value = 0 # reset the player's and dealer's value at 0
    dealer.value = 0
    click_deal = False # reset all the buttons 
    click_hit = False 
    click_stand = False
    clicks_on_hit = 0 # reset clicks_on_hit 
    click_play_again = False # reset all variables 
    game_finished = False 
    blackjack = False
    blackjack_tie = False 
    busted_player = False
    busted_dealer = False 
    win = False
    lose = False 
    tie = False
    result = False
    show_dealer_card = False 
  
  click_next_round = False 

  pygame.display.update()

pygame.quit()      