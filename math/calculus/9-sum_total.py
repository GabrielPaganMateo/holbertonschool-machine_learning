#!/usr/bin/env python3
"""
Module with def summation function
"""


def summation_i_squared(n):
    """Summation function"""
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum