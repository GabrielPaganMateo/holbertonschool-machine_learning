#!/usr/bin/env python3
"""
Module with function that returns matrix operations
"""


def np_elementwise(mat1, mat2):
    """Perform matrix operations"""
    sum = mat1 + mat2
    difference = mat1 - mat2
    print(type(mat2))
    product = mat1 * mat2
    quotient = mat1 / mat2
    return sum, difference, product, quotient
