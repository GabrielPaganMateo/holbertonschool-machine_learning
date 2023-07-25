#!/usr/bin/env python3
"""
Module with function that concatenates two arrays
"""
def cat_arrays(arr1, arr2):
    """Function that concatenates two arrays"""
    arrOne = arr1[:]
    arrTwo = arr2[:]
    arrOne.extend(arrTwo)
    return arrOne
