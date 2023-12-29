import pygame
import random
from constants import window

blackjack1 = False
blackjack_tie1 = False 
blackjack2 = False
blackjack_tie2 = False
busted_player1 = False
busted_player2 = False 
busted_dealer = False 
win1 = False
win2 = False 
lose1 = False 
lose2 = False
tie1 = False
tie2 = False
show_dealer_card = False 


# List of card ranks and suits. Also number of decks used in the game
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']
DECK_COUNT = 3

# Create a class Deck to create the deck of carts. 
# If we create an object of the class, the function build is called and a card deck is created, consisting of the number of decks we have defined in DECK_COUNT.
class Deck:
    def __init__(self):
        self.cards = []
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
                    self.cards.append((i, value, suit))

# Shuffle method: shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)
    
# Deal method: pops a card from the deck if the deck consists of more then 1 card
# VRAAG: Waarom niet >=1? je kan nog 1 kaart delen als er nog 1 kaart overblijft. Maar dan kan je de startdeal niet doen. Ik weet niet of het belangrijk is.
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

# Hand object with empty list of cards and empty list of images. A value is set to 0
# Original function: Hand class inherits from the Deck class
# VRAAG: waarom inherits van de Deck-class? Er is geen enkele functie hierboven die je met een hand direct nodig hebt van de Deck-class.
        # Ik weet het niet zeker want ik weet niks zeker. 
        # Maar als je in een geerfde functie een nieuwe init schrijft, dan wordt de init van de parent-class overschreven. 
        # Je kan wel de functies van de parent-class toepasssen op de hand. Maar zullen we dat ergens gebruiken? 
        # bv: build: nvt, shuffle: je gaat je hand niet shuffelen, 
        # deal: je gebruikt deal wel om de hand te maken met de functie add_card, maar die kan je ook oproepen zonder dat Hand erft van Deck. 
        # Misschien mis ik iets dat later in het spel van belang zal zijn. Ik heb het nu weggelaten en het werkt evenzeer.  
class Hand:
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0
    
# Adds a card to the empty cards list
# Hide functie toegevoegd -- waarom? wat doet dat? 
    # def add_card(self, card, hide=False):
        # card_with_hide = (card[0], card[1], hide)
        # self.cards.append(card_with_hide)
    
    def add_card(self, card):
        self.cards.append(card)

# Calculates the value of the hand
# Original functie maakt eerst een lijst van de rank van de kaarten, dan een lijst van de non-aces en evt. ook nog een lijst van de aces.
# Ik denk dat het zo ook kan? 
# Ik heb het vastzetten van de ace op 1 gewijzigd: ace is 10 als de value <= 10 en anders is het 1
# self.value = 0 toegevoegd. Bij het telkens opnieuw berekenen van de hand wordt waarde op 0 gezet
    def calculate_hand(self):
        # self.value = 0           
        for card in self.cards:
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
        for card in self.cards:
            cards = card[1] + card[2]
            if cards not in self.card_img: # Nu we het deck samenstellen met het decknr erbij, kan dit blijven staan. 
                self.card_img.append(cards)

    # Function to draw the image of the card on the screen. 
    # Function to be called in the game --> see game window.
                # Veel geprobeerd met deze functie: ik heb de meest eenvoudige manier gevonden, denk ik: 
                # 1 functie om alle kaarten op te roepen.
                    # is mogelijk omdat we de decks in het speel-deck onderscheiden en geen dubbels laten voorkomen
                    # omdat we de index van card_img-list als variabele opnemen in de functie\
                    # dit betekent wel dat je die moet aangeven als je de functie oproept
                    # in het spel zal je zien dat we de functie maar oproepen als de len(card_img) lang genoeg is, anders krijg je een index out of range
                  
    def draw_card(self, card_img_index, x_pos, y_pos):  
        self.x_pos =  x_pos
        self.y_pos = y_pos

        # self.get_filename() # deze functie moet je niet hier oproepen, maar in the game zelf. 

        if len(self.card_img) > 0: 
            card_image = pygame.image.load('images/' + self.card_img[card_img_index] + '.png')
        
            card_imageRect = card_image.get_rect()
            card_imageRect.topleft = (self.x_pos, self.y_pos)

            window.blit(card_image, card_imageRect)

    # Draw the back of the card
    # Deze functie toe te passen op de 2e kaart van de dealer. 
    # Later in het spel moet dit weg/overschreven worden met de 2e kaart van de dealer 
    # (dat kan met functie draw_secondcard, maar dan wel zo te programmeren dat dit pas komt nadat de berekening moet gebeuren,.
    def hide_card(self, x_pos, y_pos): 
        self.x_pos =  x_pos
        self.y_pos = y_pos

        self.get_filename()

        if len(self.card_img) > 0: # dit is niet nodig vanwege< maar als je dit er niet bij zet en je definieert het print< dan krijg je al meteen de image van de back op je scherm
            hide_image = pygame.image.load('images/back.png')
        
            hide_imageRect = hide_image.get_rect()
            hide_imageRect.topleft = (self.x_pos, self.y_pos)

            window.blit(hide_image, hide_imageRect)

# Use the Deck and Hand classes
deck = Deck()
deck.shuffle()

# Create hands for players and the dealer
player1 = Hand()
player2 = Hand()
dealer = Hand()

# Two players list or One player list
# In het spel kan je kiezen om met 1 of met 2 spelers te spelen. 
players_oneplayergame = [player1]
players_twoplayergame = [player1, player2]

# Deal two cards to all players and dealer: 
# Afhankelijk van of het een oneplayer of twoplayergame is, de dealer krijgt altijd 2 kaarten 
# Tweede kaart van de dealer is verborgen
def initial_deal_oneplayergame():
    for p in players_oneplayergame:
        for i in range(2):
            p.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player1.get_filename()
    dealer.get_filename()
    player1.value = 0 
    player1.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()
        
def initial_deal_twoplayergame():
    for p in players_twoplayergame:
        for i in range(2):
            p.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player1.get_filename()
    player2.get_filename()
    dealer.get_filename()
    player1.value = 0 # if you don't set the value at 0 in the function calculate hand, you must do it here. If you set it at 0 in the function, the while loop of the dealer 17 keeps running...
    player1.calculate_hand()
    player2.value = 0 
    player2.calculate_hand()

# Deal another card to both players
# Dit is wanneer je klikt op hit, maar er moet niet bij elke speler een kaart bijkomen.
# Er moet alleen een kaart bijkomen bij de speler als hij daar met hit om vraagt. 
# Nieuwe functie toegevoegd: stand_action en aanpassing hit_card

def hit_card(player): 
    player.add_card(deck.deal())
    player.get_filename()
    player.value = 0 
    player.calculate_hand()
    dealer.value = 0
    dealer.calculate_hand()

    # if player.value > 21 and dealer.value <= 21:
        # return "Busted, dealer wins!"
    # if player.value > 21 and dealer.value > 21:
        # return "Player and dealer both loses!"
def stand_action(): 
    show_dealer_card = True 
    dealer.get_filename()
    dealer.value = 0 
    dealer.calculate_hand()  
    while dealer.value < 17:
        dealer.add_card(deck.deal())
        dealer.value = 0
        dealer.calculate_hand() 
    dealer.get_filename()

def check_blackjack_player1():
    if player1.value == 21: 
           if dealer.value == 21: 
            blackjack_tie1 = True
           elif dealer.value != 21: 
            blackjack1 = True
    
# Checks if player is busted (>21). If player is busted, he always loses, even if dealer is busted as well. 
def check_busted_player1(): 
    if player1.value > 21:
        busted_player1 = True

# Checks the result in case there is no blackjack or player's not busted 
def check_result_player1(): 
    if dealer.value > 21: 
        busted_dealer = True 
        win1 = True 
    else: 
        if player1.value > dealer.value: 
            win1 = True 
        if player1.value == dealer.value: 
            tie1 = True                        
        if player1.value < dealer.value: 
            lose1 = True 
# def stand_action(player1, player2, dealer, deck):
    # for i, card in enumerate(dealer.cards):
        # if card[2]:
            # dealer.cards[i] = (card[0], card[1], False)

    # print(dealer.cards, dealer.value)

    # if player1.value > 21 or player2.value > 21:
        # return "Busted, dealer wins!"
    # elif player1.value > dealer.value:
       #  return "Player1 wins!"
   # elif player2.value > dealer.value:
       #  return "Player2 wins!"
    # elif dealer.value > 21 and player1.value > player2.value:
       #  return "Player1 wins!"
    # elif dealer.value > 21 and player1.value < player2.value:
        # return "Player 2 wins!"
    # elif player1.value == dealer.value and player2.value > player1.value:
        # return "Player 2 wins!"
    # elif player2.value == dealer.value and player1.value > player2.value:
        # return "player1 wins!"
    # elif player1.value == dealer.value:
        # return "Tie!"
    # elif player1.value == player2.value == dealer.value:
        # return "Tie!"
    # elif player1.value == 21:
       #  return "Blackjack, player1 wins!"
    # elif player1.value == 21 and player2.value != 21:
      #   return "Blackjack, player1 wins!"
    # elif player2.value == 21 and player2.value != 21:
       #  return "Blackjack, player2 wins!"
    # else: 
        # return "Dealer wins!"

# Calculate the total value of hands for both players and dealer
#  p in players_oneplayergame:
    # p.calculate_hand()
    
# for p in players_twoplayergame:
   #  p.calculate_hand()

# dealer.calculate_hand()