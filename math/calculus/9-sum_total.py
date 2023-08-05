#!/usr/bin/env python3
"""
Module with def summation function
"""


def summation_i_squared(n):
    """Summation function"""
    if isinstance(n, int) and n >= 1:
        return n * (n + 1) * (2 * n + 1) // 6
    else:
        return None