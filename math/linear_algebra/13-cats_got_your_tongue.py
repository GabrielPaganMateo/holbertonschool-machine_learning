#!/usr/bin/env python3
"""
Module to concatenate matrixes
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Function comment"""
    new_matrix = np.concatenate((mat1, mat2), axis)
    return new_matrix
