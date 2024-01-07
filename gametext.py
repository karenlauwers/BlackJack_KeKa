import pygame 

from constants import window, font_size1, font_size2, font_size3, dark_red, dark_grey, black

pygame.init()

# CLASS GAMETEXT 
#By creating a class, we can create different gamtexts in the game, without having to define the variables over and over again
#Every gametext in the game will have text, a type of font and a color. 
class GameText:
    def __init__ (self, text, font, color): 
        self.text = text
        self.font = font 
        self.color = color 

    # Function to draw the gametext on the screen. We only make use of the ref_pos 'center' or 'topleft'
    def draw_text(self, ref_pos, x_pos, y_pos):
        self.ref_pos = ref_pos 
        self.x_pos =  x_pos
        self.y_pos = y_pos

        gametext = self.font.render(self.text, True, self.color)
        textboxRect = gametext.get_rect()
        if ref_pos == 'center': 
            textboxRect.center = (self.x_pos, self.y_pos)
        elif ref_pos == 'topleft': 
            textboxRect.topleft = (self.x_pos, self.y_pos)
        window.blit(gametext, textboxRect)

#-- END OF CLASS GAMETEXT --
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
            
# GAME TEXTS  
#Welcome display & players input their name
welcome = GameText('Welcome', font_size3, dark_red)
name_question = GameText('What is your name?', font_size2, dark_red)
name_explanation = GameText('Click on the box and enter your name.', font_size1, black)

#Bet display 
bet_title = GameText('Make a bet', font_size3, dark_red)
disclaimer = GameText('Your bet must be lower than 1000. You will play 5 rounds with this bet.', font_size1, black)
explanation = GameText('Click the box and enter a number between 1 en 999. To change your bet, use backspace.', font_size1, black)
player_text = GameText('Player', font_size2, dark_red)

#Game display
# player = use the object 'player' that we already created (zie hierboven)
gametitle = GameText('KeKa\'s BlackJack', font_size2, dark_red)
bet = GameText('Bet', font_size2, dark_grey)
hand_value = GameText('Value', font_size2, dark_grey)
dealer_text = GameText('Dealer', font_size2, dark_red)

#Results 
blackjack_text = GameText('Blackjack!', font_size2, dark_red)
tie_text = GameText('It\'s a tie.', font_size2, dark_red) 
win_text = GameText('You win!', font_size2, dark_red) 
lose_text = GameText('You lose!', font_size2, dark_red) 
busted_text = GameText('You\'re busted!', font_size2, dark_red )
