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
#welcome display & players input their name
welcome = GameText('Welcome', font_size3, dark_red)
name_question = GameText('What is your name?', font_size2, dark_red)
name_explanation = GameText('Click on the box and enter your name.', font_size1, black)

#bet display 
bet_title = GameText('Make a bet', font_size3, dark_red)
disclaimer = GameText('For the sake of your bank account, your bet must be lower than 1000.', font_size1, black)
explanation = GameText('Click the box and enter a number between 1 en 999. To change your bet, use backspace.', font_size1, black)
player_text = GameText('Player', font_size2, dark_red)

#game display
# player = use the object 'player' that we already created (zie hierboven)
gametitle = GameText('KeKa\'s BlackJack', font_size2, dark_red)
bet = GameText('Bet', font_size2, dark_grey)
hand_value = GameText('Value', font_size2, dark_grey)
hand_text = GameText('Hand', font_size1, dark_grey)
split_hand_text = GameText('Split Hand', font_size1, dark_grey)
dealer_text = GameText('Dealer', font_size2, dark_red)

#results 
blackjack_text = GameText('Blackjack!', font_size2, dark_red)
tie_text = GameText('It\'s a tie.', font_size2, dark_red) 
win_text = GameText('You win!', font_size2, dark_red) 
lose_text = GameText('You lose!', font_size2, dark_red) 
busted_text = GameText('You\'re busted!', font_size2, dark_red )
test = GameText('Trying to play again', font_size5, white)
