#!/usr/bin/env python3
"""
Module with def summation function
"""


def summation_i_squared(n):
    # base case: if n is not a valid number, return None
    if not isinstance(n, int) or n < 1:
        return None
    # base case: the sum of the first 1 natural number's squares is 1
    elif n == 1:
        return 1
    else:
        # recursive case: the sum is n^2 plus the sum of the squares of the first n-1 natural numbers
        return n**2 + summation_i_squared(n-1)