RED = 'red'
BLACK = 'black'
COLORS = [RED, BLACK]


class Easy21(object):
    """Easy21 game manager.
    >>> game = Easy21()
    >>> while not game.is_end():
    ...     game.stick() # or game.hit()
    """
    _dealer = []
    _player = []

    def __init__(self):
        # initialize state
        pass

    def is_end(self):
        # return true if game is not continuing
        pass

    def state(self):
        # return state : dealer's first card and all of players cards
        pass

    def stick(self):
        # do action stick
        pass

    def hit(self):
        # do action do
        pass

    def _step(self, action):
        # do action
        # setup next state (draw card)
        pass


class Card(object):
    def __init__(self, number=None, color=None):
        # set color, number
        # if not set, pick random
        pass
