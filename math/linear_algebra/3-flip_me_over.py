#!/usr/bin/env python3
"""
Module with function that transposes
"""


def matrix_transpose(matrix):
    """Function that transposes"""
    new_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix
