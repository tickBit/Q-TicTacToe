import random
import datetime
import numpy as np
from q import Q
from tictactoe import TicTacToe

class Agent:

    def __init__(self, ALPHA, GAMMA):
        self.epsilon = 1.0
        self.qagent = Q(ALPHA, GAMMA)
        self.rewards_pos = []
        self.rewards_draw = []
        self.rewards_neg = []

        random.seed(42)

    def get_action(self, state, valid_actions):

        # Exploration or exploitation
        if random.random() < self.epsilon:
            return random.choice(valid_actions)
        best = self.qagent.get_q_action(state)

        if best is None:
            return random.choice(valid_actions)
        
        return best
    
    def learn(self, EPOCHS):
        env = TicTacToe()

        min_epsilon = 0.01
        max_epsilon = 1.0
        decay_rate = 0.001

        for episode in range(EPOCHS):
            pos_rewards = 0
            draws = 0
            neg_rewards = 0

            _ = env.reset()

            while True:
                state = env.getState()
                action = self.get_action(state, env.getValidMoves())
                winner = env.play(action)

                if winner or env.isDraw():
                    if winner == 1: pos_rewards += 1
                    if env.isDraw: draws += 1

                    self.qagent.update(state, action, env.getState(), 100)
                    break

                winner = env.play(random.choice(env.getValidMoves()))
                if winner or env.isDraw():
                    if winner == -1: neg_rewards += 1
                    if env.isDraw(): draws += 1


                    self.qagent.update(state, action, env.getState(), -100)
                    break
                self.qagent.update(state, action, env.getState(), 0)

            self.rewards_pos.append(pos_rewards)
            self.rewards_neg.append(neg_rewards)
            self.rewards_draw.append(draws)

            if self.epsilon > min_epsilon: self.epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
            
            if episode % 1000 == 0: print("Epoch", episode, "Epsilon", self.epsilon)

            