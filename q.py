from collections import defaultdict

class Q:

    def __init__(self, ALPHA, GAMMA):
        self.ALPHA = ALPHA      # learning rate
        self.GAMMA = GAMMA      # discount rate
        self.q_table = defaultdict(defaultdict)

        # the initial state is set to 0.0, if you want to emphasize position 4, set other values initially for example to -1.0
        for i in range(9):  
            self.q_table["[0 0 0 0 0 0 0 0 0]"][i] = 0.0

    # update the Q-table with a new Q value
    def update(self, state, action, next_state, reward):
        # get old Q-value
        value = 0.0

        try:
            value = self.q_table[state][action]
        except KeyError:
            # if a state doesn't exist, it is initialized with all actions to 0.0
            for i in range(9):
                self.q_table[state][i] = 0.0
            
        v = list(self.q_table[next_state].values())
        
        #..apply the Bellman's equation
        next_q = max(v) if v else 0
        value = value + self.ALPHA * (reward + self.GAMMA * next_q - value)
        
        self.q_table[state][action] = value

    def get_Q_table(self):
        return self.q_table

    # get the key of best Q-value for a position a on the game board
    def get_q_action(self, state):
        table = self.q_table[state]
        if not table:
            return None
        return max(table, key=table.get)