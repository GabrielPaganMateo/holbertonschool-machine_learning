#!/usr/bin/python3 env
"""
Module with def summation function
"""


def summation_i_squared(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum