import random
import datetime
import numpy as np
from q import Q
from tictactoe import TicTacToe

class Agent:

    def __init__(self, ALPHA, GAMMA, EPOCHS):
        self.epsilon = 1.0
        self.qagent = Q(ALPHA, GAMMA)
        self.rewards_pos = []
        self.rewards_draw = []
        self.rewards_neg = []
        self.rnd_numbers = []
        self.epsilons = []
        self.epochs = EPOCHS
        self.explorations = 0
        self.rounds = 0
        self.games = 0

        #random.seed(datetime.datetime.now().timestamp())
        random.seed(111)
    
    def get_action(self, state, valid_actions, episode):

        self.rounds += 1

        # You can experiment with this to balance between exploration and exploitation

        rnd = random.random()

        # Exploration or exploitation
        if rnd < self.epsilon:
            self.explorations += 1
            return random.choice(valid_actions), rnd
        best = self.qagent.get_q_action(state)

        if best is None:
            return random.choice(valid_actions), rnd
        
        return best, rnd
    
    def get_epsilons_rnds(self):
        return self.epsilons, self.rnd_numbers
    
    def learn(self):
        env = TicTacToe()

        min_epsilon = 0.01
        max_epsilon = 1.0
        decay_rate = 0.001

        for episode in range(self.epochs):
            pos_rewards = 0
            draws = 0
            neg_rewards = 0

            _ = env.reset()

            while True:
                state = env.getState()
                action, rnd = self.get_action(state, env.getValidMoves() , episode)
                winner = env.play(action)

                if winner or env.isDraw():
                    if winner == 1: pos_rewards += 1
                    if env.isDraw(): draws += 1

                    self.games += 1

                    self.qagent.update(state, action, env.getState(), 100)
                    break

                winner = env.play(random.choice(env.getValidMoves()))
                if winner or env.isDraw():
                    if winner == -1: neg_rewards += 1
                    if env.isDraw(): draws += 1

                    self.games += 1

                    self.qagent.update(state, action, env.getState(), -100)
                    break
                self.qagent.update(state, action, env.getState(), 0)

                self.rnd_numbers.append(rnd)
                self.epsilons.append(self.epsilon)

                self.games += 1

            self.rewards_pos.append(pos_rewards)
            self.rewards_neg.append(neg_rewards)
            self.rewards_draw.append(draws)

            
            self.epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
            if episode % 1000 == 0: print("Epoch", episode, "Epsilon", self.epsilon, "Random number", rnd, "Epsilon < random number: ", self.epsilon < rnd)

        print("Exploration rate: ", round(self.explorations / self.rounds, 4))