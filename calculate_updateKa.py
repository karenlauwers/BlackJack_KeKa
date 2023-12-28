import pygame
from blackjack_deck_updateKa import Deck, Hand

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
    dealer.add_card(deck.deal(), hide=True)
    
def initial_deal_twoplayergame():
    for p in players_twoplayergame:
        for i in range(2):
            p.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal(), hide=True)

# Deal another card to both players
# Dit is wanneer je klikt op hit, maar er moet niet bij elke speler een kaart bijkomen.
# Er moet alleen een kaart bijkomen bij de speler als hij daar met hit om vraagt. 
# Nieuwe functie toegevoegd: stand_action en aanpassing hit_card

def hit_card(player): 
    player.add_card(deck.deal())

    if player.value > 21 and dealer.value <= 21:
        return "Busted, dealer wins!"
    if player.value > 21 and dealer.value > 21:
        return "Player and dealer both loses!"

def stand_action(player1, player2, dealer, deck):
    for i, card in enumerate(dealer.cards):
        if card[2]:
            dealer.cards[i] = (card[0], card[1], False)
    while dealer.value < 17:
        dealer.add_card(deck.deal())
        dealer.calculate_hand()

    print(dealer.cards, dealer.value)

    if player1.value > 21 or player2.value > 21:
        return "Busted, dealer wins!"
    elif player1.value > dealer.value:
        return "Player1 wins!"
    elif player2.value > dealer.value:
        return "Player2 wins!"
    elif dealer.value > 21 and player1.value > player2.value:
        return "Player1 wins!"
    elif dealer.value > 21 and player1.value < player2.value:
        return "Player 2 wins!"
    elif player1.value == dealer.value and player2.value > player1.value:
        return "Player 2 wins!"
    elif player2.value == dealer.value and player1.value > player2.value:
        return "player1 wins!"
    elif player1.value == dealer.value:
        return "Tie!"
    elif player1.value == player2.value == dealer.value:
        return "Tie!"
    elif player1.value == 21:
        return "Blackjack, player1 wins!"
    elif player1.value == 21 and player2.value != 21:
        return "Blackjack, player1 wins!"
    elif player2.value == 21 and player2.value != 21:
        return "Blackjack, player2 wins!"
    else: 
        return "Dealer wins!"

# Calculate the total value of hands for both players and dealer
#  p in players_oneplayergame:
    # p.calculate_hand()
    
# for p in players_twoplayergame:
   #  p.calculate_hand()

# dealer.calculate_hand()