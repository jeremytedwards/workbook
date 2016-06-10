# coding=utf-8
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    @staticmethod
    def spades_high(card):
        """
        This method ranks cards by the rule "suit_values" 0 for the 2 of clubs through
        51 for the ace of spades
        :param card:
        :return:
        """
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]