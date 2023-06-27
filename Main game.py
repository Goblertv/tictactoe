import players
from board import Board
import random


def exit_app():
    what_next = input('Do you want to start a new game?(yes or no)\n')
    if what_next == "no":
        print("ok, bye")
        exit(0)
    if what_next == "yes":
        print("starting a new game")
        one_player_game()


def check(board, shape, name, player):
    if player.check_if_win(board, shape) is True:
        print(f"{name} win!")
        exit_app()
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
                        exit_app()


def add(x, y, shape, board):
    board.add_to_board(x, y, shape)
    board.print_board()


def one_player_game():
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
        add(h_x, h_y, shape, board)
        if check(board.board, shape, name, player):
            exit_app()
        b_x, b_y = bot.check_if_gonna_win(board.board, b_shape, 0, shape, 0, {})
        add(b_x, b_y, b_shape, board)
        if check(board.board, shape, name, player):
            exit_app()


def two_players_game():
    possible_shapes = ["X", "O"]
    board = Board()
    name_1 = input('the first player will enter is name now\n')
    name_2 = input('now the second player will enter his name\n')
    starter, second = None, None
    name_lst = [name_1, name_2]
    shape_1 = random.choice(possible_shapes)
    possible_shapes.remove(shape_1)
    shape_2 = possible_shapes[0]
    print(f"{name_1} shape is {shape_1} and {name_2} is {shape_2}")
    player_1 = players.HumanPlayer(name_1, shape_1, board.board)
    player_2 = players.HumanPlayer(name_2, shape_2, board.board)
    random_start = random.choice(name_lst)
    if random_start == name_1:
        starter = player_1
        second = player_2
    if random_start == name_2:
        starter = player_2
        second = player_1
    print(f"{random_start} will go first")
    while True:
        h_x_1, h_y_1 = starter.player_next_move()
        add(h_x_1, h_y_1, starter.shape, board)
        check(board.board, starter.shape, starter.name, starter)
        h_x_2, h_y_2 = second.player_next_move()
        add(h_x_2, h_y_2, second.shape, board)
        check(board.board, second.shape, second.name, second)
        
    
def decide():
    decision = input("do you want to play this one vs one or against the computer (write c or h)\n")
    while True:
        if decision == "c":
            one_player_game()
        elif decision == "h":
            two_players_game()
        else:
            decision = input("please enter human or computer by what you want")


decide()
