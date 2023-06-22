import players
from board import Board


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


def add(x, y, shape, board, is_h):
    board.add_to_board(x, y, shape, is_h)
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
            bot = players.AIPlayer('O', shape, board.board)
            player = players.HumanPlayer(name, shape, board.board)
            is_ok = True
        elif shape == 'O':
            b_shape = 'X'
            bot = players.AIPlayer('X', shape, board.board)
            player = players.HumanPlayer(name, shape, board.board)
            is_ok = True
        else:
            pass

    while True:
        h_x, h_y = player.player_next_move()
        add(h_x, h_y, shape, board, True)
        if call_check_win(board.board, shape, name, player):
            exit_app()
        b_x, b_y = bot.check_if_gonna_win(board.board, b_shape, 0, shape, 0, {})
        add(b_x, b_y, b_shape, board, False)
        if call_check_win(board.board, shape, name, player):
            exit_app()


main_game()
