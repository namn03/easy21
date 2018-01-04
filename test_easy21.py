from unittest import TestCase
from easy21 import Easy21, Card, COLORS


class TestEasy21(TestCase):
    def test_initialization(self):
        for i in range(30):
            game = Easy21()
            state = game.state()

            # [ dealer's card  [player's cards] ]
            self.assertEqual(type(state), 'list')
            self.assertEqual(len(state), 2)

            self.assertIsInstance(state[0], Card)
            self.assertTrue(1 <= state[0].number <= 10)
            self.assertTrue(state[0].color in COLORS)

            self.assertEqual(type(state[1]), 'list')
            self.assertEqual(len(state[1]), 1)

            self.assertIsInstance(state[1][0], Card)
            self.assertTrue(1 <= state[1][0].number <= 10)
            self.assertTrue(state[1][0].color in COLORS)

            self.assertFalse(game.is_end())
            game.stick()
            self.assertTrue(game.is_end())
