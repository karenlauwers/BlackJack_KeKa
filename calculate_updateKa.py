from blackjack_deck import Deck, Hand

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
def start_deal_oneplayergame():
    for p in players_oneplayergame:
        for i in range(2):
            p.add_card(deck.deal())
    for i in range(2):
        dealer.add_card(deck.deal())

def start_deal_twoplayergame():
    for p in players_twoplayergame:
        for i in range(2):
            p.add_card(deck.deal())
    for i in range(2):
        dealer.add_card(deck.deal())

# Deal another card to both players
# Dit is wanneer je klikt op hit, maar er moet niet bij elke speler een kaart bijkomen.
# Er moet alleen een kaart bijkomen bij de speler als hij daar met hit om vraagt. 

def hit_card(player): 
    player.add_card(deck.deal())

# Calculate the total value of hands for both players and dealer
#  p in players_oneplayergame:
    # p.calculate_hand()
    
# for p in players_twoplayergame:
   #  p.calculate_hand()

# dealer.calculate_hand()