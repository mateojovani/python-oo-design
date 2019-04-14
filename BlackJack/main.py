from Deck import Deck
from Hand import BlackJackHand
from Card import Card, BlackJackCard

# Tests
if __name__ == "__main__":
    # Init Game
    def deal():
        deck.deal(dealer_hand)
        deck.deal(player_hand)
        print("Dealer", dealer_hand)
        print("Player", player_hand)

    deck = Deck(Card=BlackJackCard, shuffle=True)
    dealer_hand = BlackJackHand()
    player_hand = BlackJackHand()

    print("First Round")
    deal()

    print("Second Round")
    deal()

    print("Third Round")
    deal()