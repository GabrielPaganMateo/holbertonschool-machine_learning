#!/usr/bin/env python3
"""
Module with function
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Function that concatenates"""
    if len(mat1) == 0 and len(mat2) > 0:
        return mat2.copy()
    elif len(mat2) == 0 and len(mat2) > 0:
        return mat1.copy()
    elif len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    matrix1 = []
    matrix2 = []
    for i in range(len(mat1)):
        matrix1.append(mat1[i].copy())
    for i in range(len(mat2)):
        matrix2.append(mat2[i].copy())
    if axis == 0:
        for arr in matrix1:
            new_matrix.append(arr[:])
        for arr in matrix2:
            new_matrix.append(arr[:])
        return new_matrix
    elif axis == 1:
        for i in range(len(matrix1)):
            matrix1[i].extend(matrix2[i])
        new_matrix = matrix1[:]
        return new_matrix
