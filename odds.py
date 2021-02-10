'''Odds'''
from fractions import Fraction


class Odds:
    '''Odds'''

    def __init__(self, team, odds):
        self.team = team
        if odds == 'EVS':
            odds = '1/1'
        self.odds = odds
        self.decimal_odds = Fraction(odds) + 1

    def __repr__(self):
        decimal_odds = float(self.decimal_odds)
        return f'{self.team} at {self.odds} ({decimal_odds:.2f})'
