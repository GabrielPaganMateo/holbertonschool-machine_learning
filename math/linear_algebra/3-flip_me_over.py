#!/usr/bin/env python3
"""
Module with function that transposes
"""
def matrix_transpose(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            try:
                row.append(matrix[j][i])
            except IndexError:
                return new_matrix
        new_matrix.append(row)
    return new_matrix
