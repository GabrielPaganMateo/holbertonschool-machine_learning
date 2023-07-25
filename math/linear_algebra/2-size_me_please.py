#!/usr/bin/env python3
"""Function that calculates the shape of a matrix"""
from numpy import shape, array
def matrix_shape(matrix):
    shapeOfmatrix = array(matrix)
    shapeOfmatrix = shape(shapeOfmatrix)
    return list(shapeOfmatrix)
