from fractions import Fraction

class Odds:
    def __init__(self, team, odds):
        self.team = team
        if (odds == 'EVS'):
            odds = '1/1'
        self.odds = odds
        self.decimal_odds = Fraction(odds) + 1

    def __repr__(self):
        return self.team + " at " + str(self.odds) + " (" + str("{:.2f}".format(float(self.decimal_odds))) + ")"