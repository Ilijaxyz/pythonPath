class Card:
  allowed_suits = ("Hearst", "Dimonds", "Clubs", "Spades")
  allowed_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
  def __init__(self, suit, value):
    if suit not in Card.allowed_suits:
      raise ValueError("Not allowed suit")
    elif value not in Card.allowed_values:
      raise ValueError("Not allowed value")
    self.suit = suit
    self.value = value
  def __repr__(self):
    return f"{self.value} of {self.suit}"
