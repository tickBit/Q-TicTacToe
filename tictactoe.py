import numpy as np

class TicTacToe:
    
    def __init__(self):
        self.board = np.array([0 for _ in range(9)])
        self.turn = 1
    
    def render(self):
        board = self.board.reshape(3,3)
        
        for j in range(3):
            row = ""
            for i in range(3):
                if board[j][i] == 0: row += "."
                if board[j][i] == 1: row += "X"
                if board[j][i] == -1: row += "O"
            print(row)

    def reset(self):

        self.board = np.array([0 for _ in range(9)])

        self.turn = 1

        return str(self.board)
    
    def getState(self):
        return str(self.board)

    def setMove(self, action):
        self.board[action] = self.turn
        
        winner = self.get_winner()

        if winner:
            return winner

        # also switch the player
        self.turn = -self.turn

        return None
    
    def getTurn(self):
        return self.turn
    
    def isFull(self):

        for i in range(len(self.board)):
            if self.board[i] == 0: return False
        return True

    def get_winner(self):

        board = self.board.reshape(3,3)
        # check horizontal
        for i in range(3):
            if abs(sum(board[i])) == 3:
                return board[i][0]

        # check vertical
        for i in range(3):
            if abs(sum(board[j][i] for j in range(3))) == 3:
                return board[0][i]

        # check diagonal
        if abs(sum(board[i][i] for i in range(3))) == 3:
            return board[0][0]
        if abs(sum(board[i][2 - i] for i in range(3))) == 3:
            return board[0][2]

        return None


    def isDraw(self):

        # if the board is full and winner == None, it's a tie
        if self.isFull() == True and self.get_winner() == None:
            return True
        else:
            return False
        
    def getValidMoves(self):
        actions = []
    
        for i in range(len(self.board)):
            if self.board[i] == 0: actions.append(i)

        return actions

    def play(self, p):
        
        if self.board[p] != 0:
            return None

        self.board[p] = self.turn
        
        winner = self.get_winner()

        if winner: return winner

        # also switch the player
        self.turn = -self.turn

        return None
    