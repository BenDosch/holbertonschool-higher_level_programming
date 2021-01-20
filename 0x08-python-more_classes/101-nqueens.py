#!/usr/bin/python3

#Helper to check valid placement

def check(board, n, row, col):
    if row >= n or col >= n:
        return False
    #check if Q exists in row
    if "Q" in board[row]:
        return False
    #check if Q exists in col
    elif "Q" in board[col]:
        return False
    #check if Q exists in diagonal... 4 directions?

    else:
        return True

#body

def solve(board, n, row, col):

#base case
    #when we reach last col of last row
    if (check(board, n, row, col)) and row == n - 1:
        board[row][col] = "Q"
        for i in range(n):
            print("{}".format(board[i]))
        return False

#body
    #check if we reached the last col
    if col == n - 1:
        #go to next row (recurs on row)
        solve(board, n, row + 1, 0)
    else:
        #check if cell is a valid placement for a queen
        if (check(board, n, row, col)):
            #set value of a cell to Q
            board[row][col] = "Q"
        #go to next col (recurse on col)
        solve(board, n, row, col + 1)
    return

def n_queens(n):

    #check n > 4 & a number ect..
    if n < 4:
        print("N must be at least 4")
        exit(1)

    """create a blank square of size n"""
    board = [[0 for x in range(n)] for y in range(n)]
    print(board)
    solve(board, n, 0, 0)


if __name__ == "__main__":

    n_queens(4)
