import pygame
import random
from constants import window

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
# Hide functie toegevoegd
    def add_card(self, card, hide=False):
        card_with_hide = (card[0], card[1], hide)
        self.cards.append(card_with_hide)

# Calculates the value of the hand
# Original functie maakt eerst een lijst van de rank van de kaarten, dan een lijst van de non-aces en evt. ook nog een lijst van de aces.
# Ik denk dat het zo ook kan? 
# Ik heb het vastzetten van de ace op 1 gewijzigd: ace is 10 als de value <= 10 en anders is het 1
# self.value = 0 toegevoegd. Bij het telkens opnieuw berekenen van de hand wordt waarde op 0 gezet
    def calculate_hand(self):
        self.value = 0           
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
            if cards not in self.card_img: # in ons spel met 3 decks of cards kan het wel dat je 2 dezelfde kaarten hebt... en dan wordt die in huidige opzet niet op het scherm getekend... moet nog iets aan veranderen. Ofwel aan deze functie, ofwel aan opzet van het tekenen.  
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

        # self.get_filename()

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

