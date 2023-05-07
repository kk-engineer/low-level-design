from random import random


class Dice:
    def __init__(self):
        self._faces = None

    def roll(self) -> int:
        return random.random() % self._faces + 1
