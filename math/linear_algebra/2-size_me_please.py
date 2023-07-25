#!/usr/bin/env python3
"""Function that calculates the shape of a matrix"""
def matrix_shape(matrix):
    shape = []
    shape.append(len(matrix))
    if type(matrix[shape[0] - 1]) is list:
        for i in range(0, shape[0]):
            if i == shape[0] - 1:
                shape.append(len(matrix[i]))
                if type(matrix[i][0]) is list:
                    shape.append(len(matrix[i][0]))
    return shape
"""
[
    [
         [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]
                                                                    ],
        [
            [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]
                                                                             ]
                                                                                ]
"""