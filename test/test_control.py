from unittest import TestCase
from control import epsilon_greedy, MCControl, TDControl


class TestEpsilonGreedy(TestCase):
    def test_epsilon_greedy(self):
        for _ in range(100):
            self.assertEqual(epsilon_greedy(0, [1, 2]), 1)
            self.assertEqual(epsilon_greedy(0, [1, 0]), 0)


class TestMCControl(TestCase):
    def test_control(self):
        control = MCControl(10, 7)
        control.experience(0, 0, 10)
        control.finish_episode()

        self.assertEqual(control.Qsa[0, 0], 10)
        self.assertEqual(control.Nsa[0, 0], 1)


class TestTDControl(TestCase):
    def test_control(self):
        control = TDControl(10, 7)
        control.experience(0, 0, 10)
        control.finish_episode()

        self.assertEqual(control.Qsa[0, 0], 10)
        self.assertEqual(control.Nsa[0, 0], 1)

        control = TDControl(10, 7, lambda_val=1)
        control.experience(0, 0, 10)
        control.experience(1, 0, 20)
        control.finish_episode()

        print(control.Qsa[0, 0])
        self.assertEqual(control.Qsa[0, 0], 30)
        self.assertEqual(control.Qsa[1, 0], 20)
