from random import sample, randint

RED = 'red'
BLACK = 'black'
COLORS = [RED, BLACK]

STICK = 'stick'
HIT = 'hit'
ACTIONS = [STICK, HIT]

SCORES = list(range(1, 11))*2 + list(range(-10, 0))

TERMINATED = 'terminated'


class Easy21(object):
    """Easy21 game manager.
    >>> game = Easy21()
    >>> state, reward = game.step(HIT)
    """
    def __init__(self):
        self._dealer_sum = randint(1, 10)
        self._player_sum = randint(1, 10)

    @staticmethod
    def _draw():
        return sample(SCORES, 1)[0]

    def state(self):
        return [self._dealer_sum, self._player_sum]

    def step(self, action):
        assert(action in ACTIONS)

        if action == HIT:
            self._player_sum += self._draw()
            if not 1 <= self._player_sum <= 21:
                # player lose
                return [TERMINATED, -1]
            return [self.state(), 0]
        else:
            while self._dealer_sum < 17:
                self._dealer_sum += self._draw()

            if self._dealer_sum < self._player_sum:
                reward = 1
            elif self._dealer_sum > self._player_sum:
                reward = -1
            else:
                reward = 0

            return [TERMINATED, reward]
