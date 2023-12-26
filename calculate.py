from blackjack_deck import Deck, Hand

# Use the Deck and Hand classes
deck = Deck()
deck.shuffle()

# Create hands for players and the dealer
player1 = Hand()
player2 = Hand()
dealer = Hand()

# Two players list 
players = [player1, player2]

# Deal two cards to all players and dealer
for p in players:
    for i in range(2):
        p.add_card(deck.deal())

for i in range(2):
    dealer.add_card(deck.deal())

print('player1', player1.cards)
print('player2', player2.cards)
print('dealer', dealer.cards)

# Deal another card to both players
for p in players:
    p.add_card(deck.deal())

print('player1',player1.cards)
print('player2', player2.cards)

# Calculate the total value of hands for both players and dealer
for p in players:
    p.calculate_hand()

dealer.calculate_hand()