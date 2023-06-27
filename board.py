import numpy as np


class Board:
    def __init__(self):
        self.board = np.array([['', '', ''],
                               ['', '', ''],
                               ['', '', '']])

    def add_to_board(self, x, y, shape):
        is_ok = False
        while not is_ok:
            for i in range(len(self.board)):
                if i == x:
                    if self.board[i, y] == '':
                        self.board[i, y] = shape
                        is_ok = True
                    else:
                        xy = input("this cell is full,please enter new points for an empty cell\n")
                        x = int(xy[0])
                        y = int(xy[1])

    def print_board(self):
        print(self.board)
