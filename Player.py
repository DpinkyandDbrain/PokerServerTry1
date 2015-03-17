__author__ = 'DpinkyandDbrain'

import Card
import Hand


class Player:
    def __init__(self, buyIn):
        self.chips = buyIn

    def recieveHand(self, hand):
        self.hand = hand