import unittest
from odds import Odds

class TestOdds(unittest.TestCase):
    def test_decimal_odds(self):
        self.assertEqual(Odds('A', '1/2').decimal_odds, 3/2)

    def test_envs(self):
        self.assertEqual(Odds('A', 'EVS').decimal_odds, 2/1)

if __name__ == '__main__':
    unittest.main()
