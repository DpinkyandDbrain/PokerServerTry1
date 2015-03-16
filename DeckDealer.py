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
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    def __init__(self):
        for c in range(0, 52):
            print 'Using ' + str(c % 4) + ' with ' + str(c % 13)
            self.suit = self.suits[c % 4]
            self.deck.append(Card(self.suit, self.values[c % 13]))

    def shuffle(self, usePrint):
        numcards = random.randint(0, 51)
        if usePrint:
            print "Number of cards to shuffle " + str(numcards)
        for i in range(0, numcards - 1):
            choice1 = random.randint(0, 51)
            choice2 = random.randint(0, 51)
            if choice1 != choice2:
                if usePrint:
                    print 'Switching card ' + str(choice1) + ' with card ' + str(choice2)
                self.deck[choice1], self.deck[choice2] = self.deck[choice2], self.deck[choice1]

    def __str__(self):
        printer = ''
        for card in self.deck:
            printer += str(card)
        return printer


class DeckDealer:
    def __init__(self):
        deck = Deck()
        print deck
        deck.shuffle(False)
        deck.shuffle(False)
        deck.shuffle(False)
        deck.shuffle(False)
        print deck

if __name__ == '__main__':
    app = DeckDealer()