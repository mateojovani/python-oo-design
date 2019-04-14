class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

class BlackJackHand(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.has_ace = False
        self.min_score = self.max_score = 0

    def add(self, card):
        Hand.add(self, card)
        if (not self.has_ace):
            if card.is_ace():
                self.has_ace = True
                self.min_score += 1
                self.max_score += 11
            else:
                self.min_score += card.value
                self.max_score += card.value
        else: # already has one ace
            if card.is_ace():
                self.min_score += 1
                self.max_score += 1
            else:
                self.min_score += card.value
                self.max_score += card.value

    def get_score(self):
        if self.max_score > 21:
            return self.min_score

        return self.max_score

    def is_21(self):
        return self.get_score() == 21

    def is_busted(self):
        return self.get_score() > 21

    def __str__(self):
        hand = ""
        for card in self.cards:
            hand += str(card.value) + " "

        return f"Score: {self.get_score()} is busted: {self.is_busted()} hand: {hand}"