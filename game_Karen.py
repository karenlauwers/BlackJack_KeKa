import pygame, sys 

# IMPORT ALL FILES THAT CONTRIBUTE TO THE GAME LOOP AND THE WINDOW SETTINGS
from constants import *
from buttons import *
from user_input import * 
from gametext import * 
from deck_and_calculate_Ka import * 

# INITIALISE PYGAME
pygame.init() 

# SET THE PLAYING FIELD
pygame.display.set_caption("BlackJack")

# AID VARIABLES. To help set the game loop and window settings. 
running = True
active_nameRect = False 
click_start_game = False 
click_next_round = False 
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
clicks_on_next_round = 0 
score = 0 
click_play_again = False 
game_finished = False 
round = 1
round_finished = False 
blackjack_scorefixer = False
tie_scorefixer = False 
win_scorefixer = False 
lose_scorefixer = False

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
    if event.type == pygame.MOUSEBUTTONDOWN and start_game.check_click(): 
        click_start_game = True 
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if nameinput_playerRect.collidepoint(event.pos): 
        active_nameRect = True  

    if active_nameRect: 
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_BACKSPACE:  # define use of the backspace 
          nameinput_player = nameinput_player[:-1] 
        elif event.key and len(nameinput_player)<20: #input can be any key, max. 20 tekens
          nameinput_player += event.unicode 
        
    if event.type == pygame.MOUSEBUTTONDOWN:
      if betinput_playerRect.collidepoint(event.pos): 
        active_betRect = True
      
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

    if event.type == pygame.MOUSEBUTTONDOWN and next_round.check_click():
      click_next_round = True 
 
#--END OF EVENTS-- 
#===============================================================================================================
#===============================================================================================================
#ME DESIGN. SETTING (DRAWING AND BLITTING) THE WINDOWS 
  # SET THE MAIN WINDOW. Fill with colour 
  # Set  GAtext and buttons 
  # Start by setting the screen
  window.fill((casino_green1))
  welcome.draw_text('center', window_width/2, 70)
  gametitle.draw_text('center', window_width/2, 110)
  name_question.draw_text('center', window_width/2, 170)
  name_explanation.draw_text('center', window_width/2, 200)
  start_game.draw_button()
  quit_button.draw_button() 

  # Draw the textboxes in which the players are going to put their bet. 
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

  nameinput_playerRect.w = max(140, name_surface.get_width() + 10) #om de tekstbox breder te maken als er meer tekens gebruikt worden. Textbox wordt op 140 breedte ingesteld en schuift op als je meer tekens gebruikt. 
  
# Setings for the play-button: you can only click play if you entered a bet between 1 and 999.
  if len(nameinput_player)<1: 
    start_game.enabled = False
    start_game.draw_button()
  else: 
    start_game.enabled = True
    start_game.draw_button()       

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

#   BET WINDOW
#   Setings for the play-button: you can only click play if you entered a bet between 1 and 999.
    if betinput_player =='0' or len(betinput_player)<1: 
      bet_ok.enabled = False
      bet_ok.draw_button()
    else: 
      bet_ok.enabled = True
      bet_ok.draw_button() 
    
    if click_bet_ok: 
      bet_ok.enabled = False
      bet_ok.draw_button() 
      play.enabled = True     
 
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
    playername = GameText(f'{nameinput_player}', font_size2, dark_red)
    playername.draw_text('center', window_width/2, 60)
    hit.draw_button()
    stand.draw_button()
    dealer_text.color = dark_red
    dealer_text.draw_text('center', window_width/2, 360)
    initial_deal_button.draw_button()
    next_round.draw_button()
    quit_button.draw_button() 

    # The bet of the player's is put on the screen with an f-string. 
    # Object of class GameText is created here, because the variable betinput_player must be filled by the player(s).
    bet_player = GameText(f'Bet     {betinput_player}€', font_size1, dark_grey) 
    bet_player.draw_text('topleft', 370, 120)
    hand_value_player = GameText(f'Value  {player.value}', font_size1, dark_grey) 
    hand_value_player.draw_text('topleft', 370, 140)   
    if show_dealer_card == True:    
      hand_value_dealer = GameText(f'Value {dealer.value}', font_size1, dark_grey) 
      hand_value_dealer.draw_text('topleft', 360, 420) 

    # Draw the cards on the screen 
    # hand_text.draw_text('topleft', 100, 160)
    if len(player.card_img) > 1:  
      player.draw_card(0, 270, 180)
      player.draw_card(1, 290, 180)
    if len(player.card_img) > 2:   
      player.draw_card(2, 370, 180)
    if len(player.card_img) == 4: 
      player.draw_card(3, 450, 180)
    dealer.draw_card(0, 270, 450)
    if show_dealer_card == False : 
      dealer.hide_card(290, 450)
    elif len(dealer.card_img) > 1: 
      dealer.draw_card(1, 290, 450)
    if len(dealer.card_img) > 2:
      dealer.draw_card(2, 370, 450)
    if len(dealer.card_img) == 4: 
      dealer.draw_card(3, 450, 450)

# Result text on the screen -
# During 5 rounds, the score falls back to the score of the previous round 
# To make this work, their is another variable needed: scorefixer, a boolean that will be true if there's a result and False if the score is set. If you use blackjack win etc for this, the text will not appear on the screen anymore because of the loop.
    if blackjack or blackjack_tie or busted_player or tie or win or lose:
      show_dealer_card = True 
      hit.enabled = False
      stand.enabled = False 
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
      if round < 5: 
        round_finished = True 
        game_finished = False 
      else: 
        round_finished = False    
        game_finished = True 
      
      # End text on the screen after 5 rounds 
      if game_finished: 
        end_of_game = GameText('Thanks for playing BlackJack with us.', font_size3, yellow_gold)
        end_of_game.draw_text('center', window_width/2, 160)
        your_total_bet_was = GameText(f'Your total bet was 5 x {betinput_player}€, so {5*float(betinput_player)}€.', font_size2, black)
        your_total_bet_was.draw_text('center', window_width/2, 200) 
        your_final_score_is = GameText(f'Your final score is  {score}€.', font_size2, black)
        your_final_score_is.draw_text('center', window_width/2, 230)
        if betinput_player != '': 
          if (5*float(betinput_player)) < score: 
            your_gain = GameText(f'{nameinput_player}, your gain is {score - (5*float(betinput_player))}€!.', font_size3, black)
            your_gain.draw_text('center',window_width/2, 270)
          elif (5*float(betinput_player)) == score: 
            break_even = GameText(f'{nameinput_player}, you are break even.', font_size3, black)
            break_even.draw_text('center', window_width/2, 270)
          elif (5*float(betinput_player)) > score: 
            your_loss = GameText(f'{nameinput_player}, your loss is {-(score - (5*float(betinput_player)))}€...', font_size3, black)
            your_loss.draw_text('center', window_width/2, 270)
        see_you_next_time = GameText("See you next time. Click 'quit' to leave.", font_size2, black)
        see_you_next_time.draw_text('center', window_width/2, 310)
      
    # Set information on the right bottom of the screen: information about actual round (nog niet klaar), scores (nog niert klaar)
    round_text = GameText(f'Round  {round} of 5', font_size2, white) 
    round_text.draw_text('topleft', 20, 480)
    score_text = GameText(f'Score   {score}€', font_size2, white)
    score_text.draw_text('topleft', 20, 520)  


#--END OF WINDOW SETTING-- 
#=================================================================================================================
#=================================================================================================================
# THE GAME 
  # INITIAL DEAL: 
  if click_initial_deal == True: # becomes True by clicking on the button "deal cards", zie event loop
    round_playing = True 
    hit.enabled = True 
    hit.draw_button()
    stand.enabled = True
    hit.draw_button()
    initial_deal()
    if player.value == 21: 
      if dealer.value == 21: 
        blackjack_tie = True
        tie_scorefixer  = True 
      elif dealer.value != 21: 
        blackjack = True
        blackjack_scorefixer = True

  click_initial_deal = False   

  if len(player.cards_hand) == 2: 
    initial_deal_button.enabled = False
    initial_deal_button.draw_button()
    
  # if player clicks hit1 for hand 1
  if click_hit == True: 
    clicks_on_hit += 1
    hit_card()
    if player.value > 21:
      busted_player = True
      lose_scorefixer = True 
    if player.value == 21: 
      if dealer.value == 21:
        tie = True 
        tie_scorefixer = True 
      if dealer.value < 21: 
        win = True 
        win_scorefixer = True 
    if clicks_on_hit == 2: 
      hit.enabled = False 
      hit.draw_button()
      stand.enabled = False 
      stand_action()
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

  click_hit = False 
       
  if click_stand == True:  
    stand.enabled = False 
    stand_action() 
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

  click_stand = False 

  if round_finished: 
    next_round.enabled = True
    next_round.draw_button()
    round_finished = False # zo wordt de next_round-button terug op inactief gezet en kan je niet meer op next round klikken tot de ronde gedaan is
  if game_finished:
    next_round.enabled = False 
    next_round.draw_button()

  if click_next_round: 
    round += 1
    clicks_on_next_round += 1
    deck.shuffle()
    initial_deal_button.enabled = True 
    initial_deal_button.draw_button()
    next_round.enabled = False 
    next_round.draw_button
    del(player.cards_hand[:])
    del(player.card_img[:])
    del(dealer.cards_hand[:])
    del(dealer.card_img[:])
    player.calculate_hand()
    dealer.calculate_hand()
    player.value = 0 
    dealer.value = 0
    click_initial_deal = False 
    click_hit = False 
    click_stand = False
    clicks_on_hit = 0
    click_play_again = False 
    game_finished = False 
    blackjack = False
    blackjack_tie = False 
    busted_player = False
    busted_dealer = False 
    win = False
    lose = False 
    tie = False
    show_dealer_card = False 
  
  click_next_round = False 

  if clicks_on_next_round == 4: 
    game_finished = True 

  pygame.display.update()

pygame.quit()      

