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
                        print("this cell is full,please enter new points for an empty cell")

    def print_board(self):
        print(self.board)


class BasePlayer:
    def __init__(self, name, shape, board):
        self.name = name
        self.board_func = Board()
        self.shape = shape
        self.board = board

    def check_if_gonna_win(self, board, shape, w, human_shape, turns, results):
        board_c = board.copy()
        results = results
        cnt = 0
        for i in range(len(board_c)):
            for j in range(len(board_c[i])):
                if board_c[i, j] == '':
                    board_c[i, j] = shape
                    if self.check_if_win(board_c, shape):
                        if shape == self.shape:
                            results[w] = [10, i, j]
                            shape = human_shape
                        else:
                            results[w] = [-10, i, j]
                            shape = self.shape
                    elif self.check_if_win(board_c, shape) is None or self.check_if_win(board_c, human_shape) is None:
                        for x in range(len(board_c)):
                            for y in range(len(board_c[x])):
                                if board_c[x, y] != "":
                                    cnt += 1
                                    if cnt == 9:
                                        results[w] = [0, i, j]
                    else:
                        self.check_if_gonna_win(board_c, shape, w + 1, human_shape, turns + 1, results)
        for k, v in results.items():
            max_score = -1000000000
            if v[0] - turns > max_score:
                max_score = v[0]
                max_w = k
        return results[max_w][1], results[max_w][2]

    @staticmethod
    def check_if_win(board, shape):
        for i in range(len(board)):
            if (board[i, 0] == board[i, 1] == board[i, 2]) and board[i, 0] != '':
                if board[i, 0] == shape:
                    return True
                else:
                    return False

        for j in range(len(board)):
            if (board[0, j] == board[1, j] == board[2, j]) and board[0, j] != '':
                if board[0, j] == shape:
                    return True
                else:
                    return False

        if (board[0, 0] == board[1, 1] == board[2, 2]) and board[0, 0] != '':
            if board[0, 0] == shape:
                return True
            else:
                return False

        if (board[-1, -1] == board[-2, -2] == board[-3, -3]) and board[-1, -1] != '':
            if board[-1, -1] == shape:
                return True
            else:
                return False
        return None


class HumanPlayer(BasePlayer):
    def __init__(self, name, shape, board):
        super().__init__(name, shape, board)

    def player_next_move(self):
        self.board_func.print_board()
        try:
            next_move = input("please enter the next shape place by row, col (x y)\n")
            x = next_move.split()[0]
            y = next_move.split()[1]
            return int(x),int(y)
        except IndexError:
            print("please enter two numbers, row and col without a ','\n "
                  "should look like(0 1)\n")
            self.player_next_move()


class AIPlayer(BasePlayer):
    def __init__(self, shape, human_shape, board):
        self.b_shape = shape
        self.human_shape = human_shape
        super().__init__("Bot", self.b_shape, board)

    def next_move(self):
        c_board = self.board_func.board.copy()
        i, j = self.check_if_gonna_win(c_board, self.b_shape, 0, self.human_shape, 0, {})
        return i, j


def exit_app():
    what_next = input('Do you want to start a new game?(yes or no)\n')
    if what_next == "no":
        print("ok, bye")
        exit(0)
    if what_next == "yes":
        print("starting a new game")
        main_game()


def call_check_win(board, shape, name, player):
    if player.check_if_win(board, shape) is True:
        print(f"{name} win!")
        return True
    if player.check_if_win(board, shape) is False:
        print(f"The bot win, maybe you will beat him next time.")
        exit_app()
    elif player.check_if_win(board, shape) is None:
        cnt = 0
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x, y] != "":
                    cnt += 1
                    if cnt == 9:
                        print("It's a draw, try next time")


def add(x, y, shape, board):
    board.add_to_board(x, y, shape)
    board.print_board()


def main_game():
    board = Board()
    name = input('please enter your name\n')
    player = None
    bot = None
    shape = None
    is_ok = False
    b_shape = ""
    while not is_ok:
        if shape != 'X' or shape != 'o':
            shape = input("please enter what shape you want (capital x (X) or capital o (O)\n")
        if shape == 'X' or shape == 'o':
            is_ok = True

        if shape == 'X':
            b_shape = 'O'
            bot = AIPlayer('O', shape, board.board)
            player = HumanPlayer(name, shape, board.board)
            is_ok = True
        elif shape == 'O':
            b_shape = 'X'
            bot = AIPlayer('X', shape, board.board)
            player = HumanPlayer(name, shape, board.board)
            is_ok = True
        else:
            pass

    while True:
        h_x, h_y = player.player_next_move()
        add(h_x, h_y, shape, board)
        if call_check_win(board.board, shape, name, player):
            exit_app()
        b_x, b_y = bot.next_move()
        add(b_x, b_y, b_shape, board)
        if call_check_win(board.board, shape, name, player):
            exit_app()


def check():
    board = np.array([['O', '', 'X'],
                      ['X', '', 'X'],
                      ['', 'O', 'O']])
    shape = 'X'
    call_ai = AIPlayer(shape, '0', board)
    call_ai.next_move()
    print(board)


main_game()
