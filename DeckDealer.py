__author__ = 'colin'

import random


class Card:
    def __init__(self, suit, value):
        """
        :param suit:
        :param value:
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' of ' + self.suit + '\n'


class Deck:

    suits = ['DI', 'HE', 'SP', 'CL']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [52]

    def __init__(self):
        for c in range(0, 51):
            self.suit = self.suits[c % 4]
            self.deck[c] = Card(self.suit, self.values[c % 13])

    def shuffle(self):
            numcards = random.randint(0, 51)
            print "Number of cards to shuffle" + numcards
            for i in range(0, numcards):
                choice1 = random.randint(1, 52)
                choice2 = random.randint(1, 52)
                if choice1 != choice2:
                    card1 = self.deck[choice1]
                    card2 = self.deck[choice2]
                    print "Switching " + card1 + " with " + card2
                    self.deck[choice1] = card2
                    self.deck[choice2] = card1


class DeckDealer:
    def __init__(self):
        deck = Deck()
        print deck
        deck.shuffle()
        deck.shuffle()
        deck.shuffle()
        deck.shuffle()
        print deck

if __name__ == '__main__':
    app = DeckDealer()
    app.MainLoop()