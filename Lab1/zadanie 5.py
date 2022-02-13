import random
from time import sleep


def display_board(board):
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(board[1], board[2], board[3]))
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(board[4], board[5], board[6]))
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(board[7], board[8], board[9]))
    print("-------------------")


def pick_a_player():
    player1 = input("Choose a player (O or X): ")
    while True:
        if player1.upper() == "X":
            player2 = "O"
            print("player 1: X, player 2: O")
            return player1.upper(), player2
        elif player1.upper() == "O":
            player2 = "X"
            print("player 1: O, player 2: X")
            return player1.upper(), player2
        else:
            player1 = input("Wrong input. Choose O or X: ")


def players_choice(cur_player):
    number = int(input("choose place: "))
    while True:
        if board[number] == ' ':
            board[number] = cur_player
            positions[cur_player].append(number)
            empty_board.remove(number)
            break
        else:
            number = int(input("choose free place: "))
            continue


def who_won(positions, cur_player):
    win_options = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for options in win_options:
        if all(pos in positions[cur_player] for pos in options):
            return True
    return False


def art_intel(cur_player):
    move = random.choice(empty_board)

    board[move] = cur_player
    positions[cur_player].append(move)
    empty_board.remove(move)
    sleep(1)


if __name__ == "__main__":
    print("--- Tic Tac Toe ---")
    print("choose type(1/2): ")
    print("1. vs computer " + "2. person vs person: ")
    type = int(input())
    players = pick_a_player()
    round = 1
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    positions = {'X': [], 'O': []}
    empty_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board(board)

    while True:
        if round % 2 == 0:
            cur_player = players[1]
            print("It's " + cur_player + " turn: ")
            if type == 1:
                art_intel(cur_player)
            elif type == 2:
                players_choice(cur_player)
        else:
            cur_player = players[0]
            print("It's " + cur_player + " turn: ")
            players_choice(cur_player)

        display_board(board)
        if who_won(positions, cur_player):
            print("------------------")
            print("\t" + cur_player + " won!!")
            print("------------------")
            break
        round += 1
        if not empty_board:
            print("\t" + "It's a draw!")
            break
