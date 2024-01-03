import pygame
import random
from constants import window

blackjack = False
blackjack_tie = False 
busted_player = False
busted_dealer = False 
win = False
lose = False 
tie = False
show_dealer_card = False 

# MAKE THE BLACKJACK DECK OUT OF 3 CARD DECKS: A CLASS. 
# List of card ranks and suits. Also number of decks used in the game
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']
DECK_COUNT = 3

# Create a class Deck to create the deck of carts. 
# If we create an object of the class, the function build is called and a card deck is created, consisting of the number of decks we have defined in DECK_COUNT.
class Deck:
    def __init__(self):
        self.cards_deck = []
        self.build()

# Build function: populates cards list with value from the list RANKS and suits from the list SUITS.
# I changed the orginal function with dictionary into a list of tuples, don't know if a dictionary is necessary? 
# + added the number of the card deck to the deck of cards. Because: 
    # in de functie display_cards: 
        # (die ik hernoemd heb naar get_filname, 
            # omdat dat in feite het enige is dat je met die functie doet. 
            # niet de kaarten displayen maar de bestandsnaam die je gaat gebruiken om de image te downloaden extraheren.}
    # zit de restrictie dat de kaart niet meer wordt toegevoegd als ze er al in zit. Dat vermijdt dubbels.
    # Dat is prima, zeker omdat de gameloop in een loop loopt, 
        # maar in ons geval met 3 decks van kaarten kan het wel dat je 2 dezelfde kaarten krijgt. 
        # Of die uit het 1e, 2e of 3e deck komen, zie je niet en als we dat niet aangeven in de opbouw van het deck, \
            # dan zijn dat voor de computer dezelfde kaarten. 
    # Dat hoeft in principe ook niet, maar met die restrictie wordt er in het geval je 2 dezelfde kaarten bedeeld krijgt, 
        # maar 1 kaart op het scherm getekend. 
    # Gemakkelijkste manier om dat op te lossen is om de 3 decks in het grote card deck van elkaar te onderscheiden. Dan kunnen er al geen dubbels meer in komen, en zijn de dubbels die wel komen er door de loop van het spel. En die hebben we niet nodig. 
    # Dit maakt dat je in de build-functie en de get_filename-functie wel naar andere indexen moet verwijzen, 
        #want index 0 is de deck nr en die hebben we niet nodig
    def build(self):
        for i in range(DECK_COUNT):
            for value in RANKS:
                for suit in SUITS:
                    self.cards_deck.append((i, value, suit))

# Shuffle method: shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards_deck)
    
# Deal method: pops a card from the deck if the deck consists of more then 1 card
# VRAAG: Waarom niet >=1? je kan nog 1 kaart delen als er nog 1 kaart overblijft. Maar dan kan je de startdeal niet doen. Ik weet niet of het belangrijk is.
    def deal(self):
        if len(self.cards_deck) > 1:
            return self.cards_deck.pop()

# CREATE HAND OF CARDS FOR PLAYER AND DEALER: A CLASS. 
class Hand:
    def __init__(self):
        self.cards_hand = []
        self.card_img = []
        self.value = 0
      
    def add_card(self, card):
        self.cards_hand.append(card)

# Calculates the value of the hand
    def calculate_hand(self):
        # self.value = 0      dit toegevoegd in de berekening van de score zelf, als je klikt. Uit te zoeken waarom ht was dat dat hier niet kan.     
        for card in self.cards_hand:
            if card[1] in 'JQK':
                self.value += 10
            elif card[1] == 'A': 
                if self.value <= 10: 
                    self.value += 11
                else: 
                    self.value +=1
            else:
                self.value += int(card[1])

    # Iteration in the cards list. Converts card's rank and suit into a string (cards): 
    # Zo wordt een lijst aangemaakt met een string 'rank suit'. Dit dient voor de opbouw van de filenaam als we de kaart op het scherm willen zetten. 
    # De filename van de files met de images van de kaarten zijn ook zo opgebouwd, bv. 10 hearts = 10H
    # Voegt de string toe aan de lijst cards_img als die nog niet bestaat. 
    def get_filename(self):
        for card in self.cards_hand:
            cards = card[1] + card[2]
            if cards not in self.card_img: # Nu we het deck samenstellen met het decknr erbij, kan dit blijven staan. 
                self.card_img.append(cards)

    # Function to draw the image of the card on the screen. 
    # Function to be called in the game --> see game window.
                                 
    def draw_card(self, card_img_index, x_pos, y_pos):  
        self.x_pos =  x_pos
        self.y_pos = y_pos

        if len(self.card_img) > 0: 
            card_image = pygame.image.load('images/' + self.card_img[card_img_index] + '.png')
        
            card_imageRect = card_image.get_rect()
            card_imageRect.topleft = (self.x_pos, self.y_pos)

            window.blit(card_image, card_imageRect)

    # Draw the back of the card
    def hide_card(self, x_pos, y_pos): 
        self.x_pos =  x_pos
        self.y_pos = y_pos

        if len(self.card_img) > 0: # dit is niet nodig vanwege< maar als je dit er niet bij zet en je definieert het print< dan krijg je al meteen de image van de back op je scherm
            hide_image = pygame.image.load('images/back.png')
        
            hide_imageRect = hide_image.get_rect()
            hide_imageRect.topleft = (self.x_pos, self.y_pos)

            window.blit(hide_image, hide_imageRect)

# USE THE DECK AND HAND CLASS
deck = Deck()
deck.shuffle()

# Create hands for players and the dealer
player = Hand()
player_hand2 = Hand() # dit is de hand die je nodig hebt voor de split. Te bekijken of je die sowieso al mee in de lisjt kan steken, ook als je de split nog niet gebruikt. Of mss moet je dan een aparte lijst maken. Nog niet geprobeerd.
dealer = Hand()

# Two players list or One player list
# In het spel kan je kiezen om met 1 of met 2 spelers te spelen. 
players = [player]

# Deal two cards to player and dealer: 
def initial_deal():
    for p in players: 
    # dit hoeft eigenlijk geen for loop meer te zijn als je maar 1 speler hebt. 
    # Wellicht mag het uiteindelijk weg. Want als er een split komt, dan doe je een deal voor 1 speler. 
    # Maar niet opnieuw voor de dealer. 
    # Ik denk dat het mss beter is om de deal voor speler en dealer apart te maken. 
    # Dan kan je de functie voor de deal aan de speler opnieuw oproepen als speler split kiest. 
        for i in range(2):
            p.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.get_filename()
    dealer.get_filename()
    player.value = 0 
    player.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()

# Deal another card als - wordt gebruikt wanneer de speler op hit klikt 
def hit_card(): 
    player.add_card(deck.deal())
    player.get_filename()
    player.value = 0 
    player.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()

def stand_action(): 
    print('dealer cards before loop', dealer.card_img)
    dealer.value = 0 
    dealer.calculate_hand()  
    while dealer.value < 17 and len(dealer.cards_hand) < 4:
        print('dealer cards after if', dealer.card_img)
        dealer.add_card(deck.deal())
        dealer.value = 0
        dealer.calculate_hand() 
    dealer.get_filename()
    print('dealer cards after loop', dealer.card_img)

def check_blackjack():
    for p in players: 
        if p.value == 21: 
           if dealer.value == 21: 
            blackjack_tie = True
           elif dealer.value != 21: 
            blackjack = True
    
# Checks if player is busted (>21). If player is busted, he always loses, even if dealer is busted as well. 
def check_busted_player1(): 
    if player.value > 21:
        busted_player = True

# Checks the result in case there is no blackjack or player's not busted 
# ik heb deze functie gemaakt om ze op te kunnen roepen in the game. Maar dat lukt me niet. 
# Als ik oproep in de game, dan doet dat niks. Ik wil nog uitzoeken hoe dat komt.
# nu heb ik deze code in the game gezet en dat werkt wel
def check_result_player1(): 
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