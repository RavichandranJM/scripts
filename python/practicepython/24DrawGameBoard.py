#!/usr/bin/env python3

def hline(size):
    return " ---" * size

def vline(size):
    return "|   " * size

def gameBoard(size):
    board = ""
    for i in range(size):
        board += hline(size) + " \n"
        board += vline(size) + "|\n"
    board += hline(size) + " \n"
    print(board)

if __name__ == "__main__":
    size = int(input("Size of the game board: "))
    gameBoard(size)
