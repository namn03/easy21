from unittest import TestCase
from easy21 import Easy21, STICK, TERMINATED


class TestEasy21(TestCase):
    def test_initialization(self):
        for i in range(30):
            game = Easy21()
            state = game.state()

            # [ dealer's sum ,  player's sum ]
            self.assertIsInstance(state, list)
            self.assertEqual(len(state), 2)

            self.assertTrue(state[0] in range(1, 11))
            self.assertTrue(state[1] in range(1, 22))

            state, reward = game.step(STICK)
            self.assertEqual(state, TERMINATED)
            self.assertTrue(reward in [-1, 0, 1])
