#!/usr/bin/python3
"""Module that contains a function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ function that takes a matrix and devides all cells by a number

    Args:
        matrix (list(list(int))): same size lists of ints inside of a list
        div (int or float): non-zero divisor for cells of matrix

    Return: a matrix of 2 decimal place floats

    """
    te_1 = "matrix must be a matrix (list of lists) of integers/floats"
    te_2 = "Each row of the matrix must have the same size"
    te_3 = "div must be a number"
    zde = "division by zero"

    if type(matrix) is not list:
        raise TypeError(te_1)
    elif not isinstance(div, (int, float)):
        raise TypeError(te_3)
    elif div == 0:
        raise ZeroDivisionError(zde)

    for row in range(len(matrix)):
        if type(matrix[row]) is not list:
            raise TypeError(te_1)
        elif len(matrix[row]) != len(matrix[0]):
            raise TypeError(te_2)
        for cell in range(len(matrix[row])):
            if not isinstance(matrix[row][cell], (int, float)):
                raise TypeError(te_1)

    new_mtx = [
        [
        (round((matrix[row][cell] / div), 2))
        for cell in range(len(matrix[row]))
        ]
        for row in range(len(matrix))
        ]

    return new_mtx
