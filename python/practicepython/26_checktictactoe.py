#!/usr/local/bin/python3.7

def check():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]
        elif board[0][row] == board[1][row] == board[2][row]:
            return board[0][row]
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
        return board[1][1]
    else:
        return None

if __name__ == '__main__':
    global board
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print("Enter the values of 3 rows tictactoe from top to bottom  seperated by comma")
    print("Ex:\n1,2,0\n1,1,0\n2,2,0\nEnter Input:\n")
    for _ in range(3):
        row = input()
        row_val = row.split(",")
        board[_][0], board[_][1], board[_][2] = row_val
    result = check()
    if result and int(result) != 0:
        print("Win by player", result)
    else:
        print("Game is draw")
