import unittest
from odds import Odds
from fractions import Fraction

class TestOdds(unittest.TestCase):
    def test_decimal_odds(self):
        self.assertEqual(Odds('A', '1/2').decimal_odds, 3/2)

    def test_envs(self):
        self.assertEqual(Odds('A', 'EVS').decimal_odds, 2/1)

    def test_decimal_odds_greater_than_1(self):
        self.assertEqual(Odds('A', '4/9').decimal_odds, Fraction('13/9'))

    def test_repr(self):
        self.assertEqual(Odds('A', '1/3').__repr__(), "A at 1/3 (1.33)")

if __name__ == '__main__':
    unittest.main()
