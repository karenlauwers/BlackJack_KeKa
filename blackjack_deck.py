import random

# List of card ranks and suits. Also number of decks used in the game
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']
DECK_COUNT = 3

# Deck object with empy list of cards and build method is called
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

# Build method: populates cards list with dictionaries. This represents each card in a deck
    def build(self):
        for _ in range(DECK_COUNT):
            for value in RANKS:
                for suit in SUITS:
                    self.cards.append({'rank': value, 'suit': suit})

# Shuffle method: shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)
    
# Deal method: pops a card from the deck
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

# Hand object with empty list of cards and empty list of images. A value is set to 0
# Hand class inherits from the Deck class
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0
    
# Adds a card to the empty cards list
    def add_card(self, card):
        self.cards.append(card)

# Calculates the value of the hand
# Aces are fixed at 1
    def calculate_hand(self):
        first_card_ranks = [a_card['rank'] for a_card in self.cards]
        non_aces = [c for c in first_card_ranks if c != 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)

        self.value += first_card_ranks.count('A')

        while self.value > 21 and 'A' in first_card_ranks:
            self.value -= 10

# Iteration in the cards list. Converts card's rank and suit into a string (cards)
# Then checks if that card image is not already in the images list. Prevents duplication
    def display_cards(self):
        for card in self.cards:
            cards = "".join((card['rank'], card['suit']))
            if cards not in self.card_img:
                self.card_img.append(cards)