import pygame 

from constants import * 
from user_input import *

pygame.init()

# CLASS GAMETEXT 
class GameText:
    def __init__ (self, text, font, color): 
        self.text = text
        self.font = font 
        self.color = color 
        # self.draw_text()  # if we enable this, the textbox and text is drawn on the screen every time we create a gametext.
                            # we don't do this, because we want to be in control of the drawing. 
                            # And for the sake of readibility and structure, we want to create all gametext in 1 preparatory file. 

    def draw_text(self, ref_pos, x_pos, y_pos):
        self.ref_pos = ref_pos 
        self.x_pos =  x_pos
        self.y_pos = y_pos

        gametext = self.font.render(self.text, True, self.color)
        textboxRect = gametext.get_rect()
        if ref_pos == 'center': 
            textboxRect.center = (self.x_pos, self.y_pos)
        else: 
            textboxRect.topleft = (self.x_pos, self.y_pos)
        window.blit(gametext, textboxRect)

# GAME TEXTS AND TEXTBOXES  
#welcome display  
welcome = GameText('Welcome to BlackJack', font_size3, dark_red)

#players input their name
# name_question = GameText('What is your name', font_size2, dark_red)

#bet display 1playergame
bet_title = GameText('Make a bet', font_size3, dark_red)
disclaimer = GameText('For the sake of your bank account, your bet must be lower than 1000.', font_size1, black)
explanation = GameText('Click the box and enter a number between 1 en 999. To change your bet, use backspace.', font_size1, black)
player1_text = GameText('Player 1', font_size2, dark_red)

#bet display 2playergame
player2_text = GameText('Player 2', font_size2, dark_grey)
betplease = GameText('Your bet, please.', font_size2, dark_red) 

#game display
# player1 = use the object 'player1' that we already created (zie hierboven)
gametitle = GameText('KeKa\'s BlackJack', font_size3, dark_red)
bet = GameText('Bet', font_size2, dark_grey)
# bet_player1 = GameText(f'{betinput_player1}', font_size2, dark_red) # must be placed in the game - after the input has been created, if not the string is still empty
# bet_player2 = GameText(f'{betinput_player2}', font_size2, dark_red)
hand_value = GameText('Value', font_size2, dark_grey)
dealer_text = GameText('Dealer', font_size2, dark_red)
score = GameText('Score', font_size2, dark_red)
round = GameText('Round', font_size2, dark_red)