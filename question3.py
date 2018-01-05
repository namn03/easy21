from easy21 import Easy21, ACTIONS, TERMINATED, CARD_MAX, PLAYER_MAX
from control import TDControl, MCControl

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


def game_state_to_control_state(game_state):
    return PLAYER_MAX*(game_state[0]-1) + game_state[1] - 1


# start learning
control = TDControl(CARD_MAX*PLAYER_MAX, len(ACTIONS))
control_mc = MCControl(CARD_MAX*PLAYER_MAX, len(ACTIONS))

for i in range(50000):
    game = Easy21(verbose=False)
    episode = []
    state = game.state()

    while state != TERMINATED:
        action = control.action(game_state_to_control_state(state))
        next_state, reward = game.step(ACTIONS[action])

        control.experience(game_state_to_control_state(state), action, reward)
        control_mc.experience(game_state_to_control_state(state), action, reward)

        # input('')
        # print(control.Qsa[game_state_to_control_state(state)][action])
        # print(control.Esa[game_state_to_control_state(state)][action])
        state = next_state

    control.finish_episode()
    control_mc.finish_episode()

    if i and i % 1000 == 0:
        print("error :", np.sum((control.Qsa - control_mc.Qsa)**2))
        print(control.Qsa[20][1])


# plot value function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(np.tile(np.arange(1, PLAYER_MAX+1), (CARD_MAX, 1)),
                  np.tile(np.arange(1, CARD_MAX+1), (PLAYER_MAX, 1)).transpose(),
                  np.max(control_mc.Qsa, 1).reshape((CARD_MAX, PLAYER_MAX)))
plt.show()

