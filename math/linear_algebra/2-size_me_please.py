#!/usr/bin/env python3
"""Module with function that calculates the shape of a matrix"""
def matrix_shape(matrix):
    """Function that calculates the shape of a matrix"""
    shape = []
    shape.append(len(matrix))
    if type(matrix[0]) is int:
        return len(matrix)
    elif type(matrix[0]) is list:
        current = (matrix_shape(matrix[0]))
        if type(current) is int:
            shape.append(current)
        elif type(current) is list:
            shape.extend(current)
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