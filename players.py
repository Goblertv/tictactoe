from board import Board


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
        try:
            next_move = input("please enter the next shape place by row, col (x y)\n")
            x = next_move.split()[0]
            y = next_move.split()[1]
            return int(x), int(y)
        except IndexError:
            print("please enter two numbers, row and col without a ','\n "
                  "should look like(0 1)\n")
            self.player_next_move()


class AIPlayer(BasePlayer):
    def __init__(self, shape, human_shape, board):
        self.b_shape = shape
        self.human_shape = human_shape
        super().__init__("Bot", self.b_shape, board)
