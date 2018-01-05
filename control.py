import numpy as np


def epsilon_greedy(epsilon, Qa):
    rand = np.random.random()
    a_star = np.argmax(Qa)

    if rand < epsilon/len(Qa) + 1 - epsilon:
        return a_star
    else:
        a = np.random.randint(0, len(Qa)-1)
        if a >= a_star:
            a += 1
        return a


class MCControl:
    def __init__(self, num_state, num_action, gamma=1, n0=100):
        self.GAMMA = gamma
        self.N0 = n0

        self.Qsa = np.zeros((num_state, num_action))
        self.Ns = np.zeros((num_state,))
        self.Nsa = np.zeros((num_state, num_action))

        self.episode = []

    def action(self, state):
        epsilon = self.N0 / (self.N0 + self.Ns[state])
        return epsilon_greedy(epsilon, self.Qsa[state])

    def experience(self, state, action, reward):
        self.episode.append([state, action, reward])

    def finish_episode(self):
        G = 0

        for state, action, reward in reversed(self.episode):
            self.Ns[state] += 1
            self.Nsa[state, action] += 1

            G = reward + self.GAMMA * G
            alpha = 1 / self.Nsa[state, action]
            self.Qsa[state, action] += alpha * (G - self.Qsa[state, action])

        self.episode = []


class TDControl:
    def __init__(self, num_state, num_action, gamma=1, n0=100, lambda_val=0):
        self.GAMMA = gamma
        self.N0 = n0
        self.LAMBDA = lambda_val

        self.Qsa = np.zeros((num_state, num_action))
        self.Esa = np.zeros((num_state, num_action))
        self.Ns = np.zeros((num_state,))
        self.Nsa = np.zeros((num_state, num_action))

        self.prev_exp = []

    def action(self, state):
        epsilon = self.N0 / (self.N0 + self.Ns[state])
        return epsilon_greedy(epsilon, self.Qsa[state])

    def experience(self, state, action, reward):
        if self.prev_exp:
            prev_state = self.prev_exp[0]
            prev_action = self.prev_exp[1]
            prev_reward = self.prev_exp[2]

            # exception : N(s, a) is zero
            alpha_sa = 1 / np.maximum(self.Nsa, np.ones(self.Nsa.shape))
            target_err = prev_reward + self.GAMMA*self.Qsa[state, action] - self.Qsa[prev_state, prev_action]
            self.Qsa += target_err * np.multiply(alpha_sa, self.Esa)
            self.Esa *= self.GAMMA * self.LAMBDA

        self.prev_exp = [state, action, reward]
        self.Esa[state, action] += 1
        self.Ns[state] += 1
        self.Nsa[state, action] += 1

    def finish_episode(self):
        prev_state = self.prev_exp[0]
        prev_action = self.prev_exp[1]
        prev_reward = self.prev_exp[2]

        # exception : N(s, a) is zero
        alpha_sa = 1 / np.maximum(self.Nsa, np.ones(self.Nsa.shape))
        # Q(terminated, a) = 0
        target_err = prev_reward - self.Qsa[prev_state, prev_action]
        self.Qsa += target_err * np.multiply(alpha_sa, self.Esa)

        self.prev_exp = []
        self.Esa.fill(0)
