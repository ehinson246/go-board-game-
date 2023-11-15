#!/usr/bin/env python3

import random
import re

board_position = []

def generate_empty_board():
    for i in range(1, 82):
        board_position.append(0)

def translate_board_position():
    translated_board = []
    for i in range(0, 81):
        value = board_position[i]
        if not (value & 4):
            translated_board.append("_")
        elif value & 16:
            translated_board.append("X")
        elif value & 8:
            translated_board.append("O")
    return translated_board

def print_board_position():
    translated_board = translate_board_position()
    row_1 = translated_board[0:9]
    row_2 = translated_board[9:18]
    row_3 = translated_board[18:27]
    row_4 = translated_board[27:36]
    row_5 = translated_board[36:45]
    row_6 = translated_board[45:54]
    row_7 = translated_board[54:63]
    row_8 = translated_board[63:72]
    row_9 = translated_board[72:81]
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    print(row_6)
    print(row_7)
    print(row_8)
    print(row_9)

def choose_colors():
    while True:
        color_choice_str = input("Please choose a color (ether white or black) to play\n(type 'white' or 'black' to choose): ")
        if color_choice_str == 'white':
            print("You have chosen the white pieces, so the computer will take the first turn.")
            computer_color = 9
            player_color = 18
            break
        elif color_choice_str == 'black':
            print("You have chosen the black pieces, so you will take the first turn.")
            computer_color = 10
            player_color = 17
            break
        else:
            print("Invalid input.")
            continue
    print("Please note that your pieces will be marked with an 'X'\nwhile the computer's moves will be maked with an 'O'.")
    return (computer_color, player_color)

colors = choose_colors()
computer_color = colors[0]
player_color = colors[1]

def find_occupied_squares():
    occupied_squares = []
    for i in board_position:
        if i & 4:
            coordinate = i + 1
            occupied_squares.append(coordinate)
    return occupied_squares

def find_empty_squares():
    empty_squares = []
    for coordinate in range(1, 82):
        value = board_position[coordinate - 1]
        if not (value & 4):
            empty_squares.append(coordinate)
    return empty_squares

def find_black_pieces():
    black_pieces = []
    for coordinate in range(1, 82):
        value = board_position[coordinate - 1]
        if value & 1:
            black_pieces.append(coordinate)
    return black_pieces

def find_white_pieces():
    white_pieces = []
    for coordinate in range(1, 82):
        value = board_position[coordinate - 1]
        if value & 2:
            white_pieces.append(coordinate)
    return white_pieces

def find_player_pieces():
    if player_color & 1:
        player_pieces = find_black_pieces()
        return player_pieces
    elif player_color & 2:
        player_pieces = find_white_pieces()
        return player_pieces

def find_computer_pieces():
    if computer_color & 1:
        computer_pieces = find_black_pieces()
        return computer_pieces
    elif computer_color & 2:
        computer_pieces = find_white_pieces()
        return computer_pieces

def make_random_computer_move():
    empty_squares = find_empty_squares()
    last_list_item = len(empty_squares) - 1
    random_list_item = random.randrange(0, last_list_item)
    coordinate = empty_squares[random_list_item]
    if computer_color & 1:
        board_position[coordinate - 1] = 13
    elif computer_color & 2:
        board_position[coordinate - 1] = 14
    print("Computer played at square " + str(coordinate))
    print_board_position()
    last_computer_move_coordinate = coordinate
    return last_computer_move_coordinate

def make_player_move():
    empty_squares = find_empty_squares()
    while True:
        move_str = input("Please input an available coordinate as your move: ")
        move_invalidation = re.search(r"\D", move_str)
        if move_invalidation is True:
            print("Invalid Input.")
            continue
        else:
            coordinate = int(move_str)
            if coordinate not in empty_squares:
                print("Invalid move -- this square is occupied.")
                continue
            else:
                if player_color & 1:
                    board_position[coordinate - 1] = 21
                    break
                elif player_color & 2:
                    board_position[coordinate - 1] = 22
                    break
    print("You played at square " + str(coordinate))
    print_board_position()
    last_player_move_coordinate = coordinate
    return last_player_move_coordinate