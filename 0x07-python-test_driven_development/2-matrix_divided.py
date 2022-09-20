#!/usr/bin/python3
"""
    2-matrix_divided.py module
    This module divides a matrix by a div number
    usage:
    >>> matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """function matrix_divided
       Args:
           matrix(array of lists)
           div(integer or float
       returns a new matrix with digits to 2dp)
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    merr = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(merr)
    if type(matrix[0]) is list:
        n = len(matrix[0])
    newmatrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(merr)
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")
        myrow = []
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(merr)
            myrow.append(round(i / div, 2))
        newmatrix.append(myrow)
    return newmatrix
