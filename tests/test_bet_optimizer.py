import unittest

from bet_optimizer import get_positive_odds, kelly_criterion_bet


class TestKellyCriterionBet(unittest.TestCase):
    def test_positive_cases(self):
        # Positive test cases
        self.assertAlmostEqual(kelly_criterion_bet(0.5, 2.0, 100), 25.00)
        self.assertAlmostEqual(kelly_criterion_bet(0.7, 1.5, 100), 50.00)
        self.assertAlmostEqual(kelly_criterion_bet(0.8, 1.2, 1000), 633.3333333333333)

    def test_negative_cases(self):
        # Negative test cases
        self.assertEqual(kelly_criterion_bet(-0.5, 2.0, 100), 0)
        self.assertEqual(kelly_criterion_bet(0.5, -2.0, 100), 0)
        self.assertEqual(kelly_criterion_bet(0.5, 2.0, -100), 0)
        self.assertEqual(kelly_criterion_bet(1.5, 2.0, 100), 0)


class TestGetPositiveOdds(unittest.TestCase):
    def test_positive_cases(self):
        # Positive test cases
        self.assertAlmostEqual(get_positive_odds(0.5), 1.0)
        self.assertAlmostEqual(get_positive_odds(0.25), 3.0)
        self.assertAlmostEqual(get_positive_odds(0.75), 0.3333333333333333)

    def test_negative_cases(self):
        # Negative test cases
        self.assertEqual(get_positive_odds(0), float("inf"))
        self.assertEqual(get_positive_odds(1), 0)
        self.assertEqual(get_positive_odds(-0.5), None)
        self.assertEqual(get_positive_odds(1.5), None)


if __name__ == "__main__":
    unittest.main()
