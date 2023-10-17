# TicTacToe with classical Q-learning

## Some instructions

- Train.ipynb can be used to train a Q-table

- The implementation relies on random initialization. My first implementation used 42 as random seed. This implementation uses current timestamp as seed. Hopefully this gives now always good results. See the Train Jupyter notebook for more info.

- Play-TicTacToe-from-saved-Q-table.py can be used to play the game with a saved Q-table

## About creating the Q-table

At first there should be more exploration, eventually more exploitation. But in case the algorithm keeps repeating itself some randomness is useful in case the algorithm doen't learn anything new anymore..