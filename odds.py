class Odds:
    def __init__(self, team, odds):
        self.team = team
        self.odds = odds

    def __repr__(self):
        return self.team + " at " + self.odds