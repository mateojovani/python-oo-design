SUITS = (
    'Club',
    'Diamond',
    'Heart',
    'Spade'
)

MAP = {
    1:  'Aces',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}

BLACK_JACK_MAP = {
    11: 10,
    12: 10,
    13: 10
}

class Card:
    def __init__(self, value, suit):
        self.value = MAP[value] if value in MAP else value
        self.suit = SUITS[suit]

    def __str__(self):
        return "Card: %s, %s" % (self.value, self.suit)

class BlackJackCard(Card):
    def __init__(self, value, suit):
        Card.__init__(self, value, suit)
        self.value = BLACK_JACK_MAP[value] if value in BLACK_JACK_MAP else value

    def is_ace(self):
        return self.value == 1

# Tests
if __name__ == "__main__":
    card1 = Card(3, 0)
    card2 = Card(12, 3)
    ace_bj = BlackJackCard(1, 0)
    print(card1)
    print(card2)
    print(ace_bj.is_ace())