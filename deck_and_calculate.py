import pygame
import random
from constants import window, ranks, suits, deck_count

# CLASS DECK 
# Create a class Deck to create the deck of carts. 
# If we create an object of the class, the function build is called and a card deck is created, consisting of the number of decks we have defined in deck_count.
class Deck:
    def __init__(self):
        self.cards_deck = []
        self.build()

# Build function: populates cards_deck-list with count from deck_count, value from the list 'ranks' and suits from the list 'suits'
# Ranks, suits and deck_count: see file 'constants' line 34
    def build(self):
        for i in range(deck_count):
            for value in ranks:
                for suit in suits:
                    self.cards_deck.append((str(i), value, suit)) # 'i' has to be a string; because concatenation (see further) between 'int' and 'str'-values is not possible. 

# Shuffle method: shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards_deck)
    
# Deal method: pops a card from the deck if the deck consists of more then 1 card
    def deal(self):
        if len(self.cards_deck) > 1:
            return self.cards_deck.pop()

#-- END OF CLASS DECK -- 
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# CLASS HAND 
# Create a class 'hand'. A set of cards that the 'self' can play with.
class Hand:
    def __init__(self):
        self.cards_hand = [] # create an empty list in which the cards of the hand will appear 
        self.card_img = [] # create a list in which we are going to create readible filenames 
        self.value = 0 # set the value of the cards at 0
    
    # Function to add a card to the hand of the player. Used in the deal, hit and dealer_action-function
    def add_card(self, card):
        self.cards_hand.append(card)

    # Calculates the value of the hand and applies the BlackJack-rules for A, J, Q and K. 
    def calculate_hand(self):
        for card in self.cards_hand:
            if card[1] in 'JQK': # refers to the second character (index 1) of each element in the list - this is the way the list is built.
                self.value += 10
            elif card[1] == 'A': 
                if self.value <= 10: 
                    self.value += 11
                else: 
                    self.value +=1
            else:
                self.value += int(card[1])

    # Prepare the drawing of the card-images on the screen. 
    # Create a list based on the list cards_hand, but instead of separated strings per element in the list, we create a new list of elements consisting of 1 string consisting of 'deck_count rank suit'. 
    # Deck_count is taking into account because otherwise the cards same cards from another deck will only be printed once on the screen. Ex: deck 3, 10 of hearts is first card, deck 2 10 of hearts is second card. If you do not take into account the deck, the card will only be drawn once - after applying function get_filename and draw_card
    # The latter part of the elements in this list will be used to refer to the filename of the card image.
    def get_filename(self):
        for card in self.cards_hand:
            cards = card[0] + card[1] + card[2]
            if cards not in self.card_img: 
                self.card_img.append(cards)

    # Function to draw the image of the card on the screen.  
    # Function is called in the file game.py GAME WINDOW SETTING, line 305              
    def draw_card(self, card_img_index, x_pos, y_pos):  
        self.x_pos =  x_pos
        self.y_pos = y_pos

        # Function will only work if there are elements in the list
            # card_img_index refers to the index of the element in the list to print out  
            # [1:] makes sure that the first character in the string (that refers to the deck_count) is removed from the string. This has to be the case because the filename only consists of ranks and suits. 
            # Notice: if the deck_count > 10, this does not work anymore. Only the first character is removed, so 0 - 9 works fine. But if deck_count should be > 10, this must be redefined. 
        if len(self.card_img) > 0: 
            card_image = pygame.image.load('images/' + self.card_img[card_img_index][1:] + '.png')
        
            card_imageRect = card_image.get_rect()
            card_imageRect.topleft = (self.x_pos, self.y_pos)

            window.blit(card_image, card_imageRect)

    # Draw the back of the card
    def hide_card(self, x_pos, y_pos): 
        self.x_pos =  x_pos
        self.y_pos = y_pos

        hide_image = pygame.image.load('images/back.png')
        
        hide_imageRect = hide_image.get_rect()
        hide_imageRect.topleft = (self.x_pos, self.y_pos)

        window.blit(hide_image, hide_imageRect)
   
#-- END OF HAND CLASS -- 
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# USE THE DECK AND HAND CLASS
# Create an instance of the Class Deck 
deck = Deck()
deck.shuffle()

# Create an instance of the Class Hand for player and dealer
player = Hand()
dealer = Hand()

# Function to deal two cards to player and dealer, prepare drawing cards on the screen & calculation of result.
# To apply in the file game.py GAME ACTIONS line 352
def deal_cards():
    for _ in range (2): 
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    player.get_filename()
    dealer.get_filename()
    player.value = 0 
    player.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()

# Deal another card if the player asks for.
# To apply in the file game.py GAME ACTIONS line 389
def hit_card(): 
    player.add_card(deck.deal())
    player.get_filename()
    player.value = 0 
    player.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()

# As long as the dealer's value is lower than 17 and the dealer's hand is less than 4 cards, the dealer will take extra cards. 
# To apply in the file game.py GAME ACTIONS line 403, 431
def dealer_action():
    dealer.value = 0 
    dealer.calculate_hand()  
    while dealer.value < 17 and len(dealer.cards_hand) < 4:
      dealer.add_card(deck.deal())
      dealer.value = 0
      dealer.calculate_hand() 
    dealer.get_filename()