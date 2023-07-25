#!/usr/bin/env python3
"""
Module with function that adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    if len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        nums1 = mat1[i]
        nums2 = mat2[i]
        new_nums = []
        for j in range(len(nums1)):
            new_nums.append(nums1[j] + nums2[j])
        new_matrix.append(new_nums)
    return new_matrix
