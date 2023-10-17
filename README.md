# TicTacToe with classical Q-learning

## Some instructions

- Train.ipynb can be used to train a Q-table

- The implementation depends on random initialization. I tried to use timestamp as random seed, but result wasn't always optimal. This version has fixed random seed. See Train Jupyter notebook for more info.

- Play-TicTacToe-from-saved-Q-table.py can be used to play the game with a saved Q-table

## About creating the Q-table

At first there should be more exploration, eventually more exploitation. But in case the algorithm keeps repeating itself some randomness is useful in case the algorithm doen't learn anything new anymore..