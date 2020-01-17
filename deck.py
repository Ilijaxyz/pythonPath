from card import Card

class Deck:
  allowed_suits = ("Hearst", "Dimonds", "Clubs", "Spades")
  allowed_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
  
  def __init__(self):
    deck = []
    for s in Deck.allowed_suits:
      for v in Deck.allowed_values:
        deck.append(Card(s,v))
    self.cards = deck
    self.count = len(deck)
  def __repr__(self):
    return f"Deck of {self.count} cards"
print(Deck())