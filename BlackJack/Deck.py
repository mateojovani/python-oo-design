from random import randint
from Card import Card, BlackJackCard

class Deck:
    def __init__(self, Card, shuffle=False):
        self.index = 0 # dealt index
        self.Card = Card # type of deck/ card constructor
        self.cards = self.set_shuffled_deck() if shuffle else self.set_ordered_deck()

    def set_ordered_deck(self):
        cards = []
        for suit in range(4):
            for num in range(1, 14):
                cards.append(self.Card(num, suit))
        return cards

    def set_shuffled_deck(self):
        cards = []
        ordered_deck = self.set_ordered_deck()

        while ordered_deck:
            cards.append(ordered_deck.pop(randint(0, len(ordered_deck)-1)))

        return cards

    def shuffle(self):
        self.cards = self.set_shuffled_deck()

    def deal(self, hand):
        hand.add(self.cards[self.index])
        self.index += 1

    def __str__(self):
        deck = "Deck \n"
        for card in self.cards:
            deck += card.__str__() + "\n"
        return deck

# Tests
if __name__ == "__main__":
    deck = Deck(Card)
    shuffled_deck = Deck(Card, shuffle=True)
    balck_jack_deck = Deck(BlackJackCard)

    print(deck)
    print(shuffled_deck)
    print(balck_jack_deck)
