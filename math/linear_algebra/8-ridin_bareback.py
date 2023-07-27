#!/usr/bin/env python3
"""
Functino that performs matrix multiplication
"""


def mat_mul(mat1, mat2):
    """Function that multiplies matrixes"""
    columns1Len = len(mat1[0])
    rows1Len = len(mat1)
    columns2Len = len(mat2[0])
    rows2Len = len(mat2)
    if columns1Len != rows2Len:
        return None
    new_matrix = []
    for i in range(rows1Len):
        empty_row = []
        for j in range(columns2Len):
            empty_row.append(0)
        new_matrix.append(empty_row)
    for i in range(rows1Len):
        for j in range(columns2Len):
            for k in range(rows2Len):
                new_matrix[i][j] += mat1[i][k] * mat2[k][j]
    return new_matrix
