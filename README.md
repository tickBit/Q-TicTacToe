# TicTacToe with classical Q-learning

## Some instructions

- Train.ipynb can be used to train a Q-table

- The implementation relies on random initialization. In my experiments the result wasn't always optimal when using current timestamp as random seed. A random number is used to determine whether to explore (randomly make a valid move) or to exploit (use the Q-table). If random number is smaller than epsilon, exploration is used, otherwise exploitation. Epsilon decreases and one should fine balance with random exploration and exploitation. At first there should be more exploration, eventually more exploitation.

- The random seed is set in the Agent class

- Play-TicTacToe-from-saved-Q-table.py can be used to play the game with a saved Q-table