import numpy as np
import pickle
from tictactoe import TicTacToe

# put here your q_table
with open('./2023-10-16-23-51-44.pickle', 'rb') as handle:
    q_table = pickle.load(handle)

env = TicTacToe()

state = env.reset()

def get_best_action(state):
    table = q_table[state]
    if not table:
        return None
    return max(table, key=table.get)
        
while True:
        state = env.getState()

        action = get_best_action(str(state))
        winner = env.play(action)
        
        print()
        env.render()
        
        if winner == -1:
            print("**** I lost (train me to be better :) )! ****")
            break
        
        if winner == 1:
             print("**** I won! ****")
             break
        
        if env.isDraw():
            print("**** It's a tie! ****")
            break
        
        ok = False
        while not ok:
            action = int(input("Your move: (valid moves: "+"".join(str(env.getValidMoves())) + ")"))
            
            if action in env.getValidMoves():
                 ok = True
            else:
                print("Not a rule of the game. Please try again.")

        winner = env.setMove(action)
        print()
        env.render()

        if winner == 1:
            print("**** I won! ****")
            break
        
        if winner == -1:
             print("**** I lost (train me to be better :) )! ****")
             break
        
        if env.isDraw():
            print("**** It's a tie! ****")
            break
