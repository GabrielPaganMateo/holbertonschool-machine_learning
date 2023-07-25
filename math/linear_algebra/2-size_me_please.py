#!/usr/bin/env python3
"""Module with function that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Function that calculates the shape of a matrix"""
    shape = []
    shape.append(len(matrix))
    if type(matrix[0]) is int:
        return [len(matrix)]
    elif type(matrix[0]) is list:
        shape.extend(matrix_shape(matrix[0]))
    return shape
