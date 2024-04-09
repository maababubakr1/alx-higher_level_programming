#!/usr/bin/python3
"""
A function that divides all elements of a matrix.

All elements of matrix should be divided by div, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    Parameters:
        - matrix(list): A list of lists of integers or floats
        - div(int or float): The divisor
    Returns:
        A new matrix.

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix has rows of different sizes
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is equal to 0
    """
    if (not isinstance(matrix, list)) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix "
                        "must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
