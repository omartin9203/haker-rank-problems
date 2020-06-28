#!/bin/python3

import math
import os
import random
import re
import sys


def rotate_ring(matrix, i, r, m, n):
    top = matrix[i][i: n-i]
    rigth = [x[n-1-i] for x in matrix[i: m-i]]
    bottom = [x for x in reversed(matrix[m-1-i][i: n-i])]
    left = [x[i] for x in reversed(matrix[i: m-i])]
    ring = top + rigth[1:] + bottom[1:] + left[1:-1]
    ring = [ring[(r + i) % len(ring)] for i in range(len(ring))]
    top = ring[0: len(top)]
    ring = ring[len(top)-1:]
    rigth = ring[0: len(rigth)]
    ring = ring[len(rigth) - 1:]
    bottom = ring[0: len(bottom)]
    ring = ring[len(bottom) - 1:]
    left = [top[0]] + [x for x in reversed(ring[0:])]
    matrix[i][i: n - i] = top
    matrix[m - 1 - i][i: n - i] = reversed(bottom)
    for index in range(len(rigth)):
        matrix[i: m - i][index][n-1-i] = rigth[index]
        matrix[i: m - i][index][i] = left[index]
    return matrix


def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(int(min(m, n)/2)):
        matrix = rotate_ring(matrix, i, r, m, n)
    for x in matrix:
        print(*x)


if __name__ == '__main__':
    # mnr = input().rstrip().split()
    #
    # m = int(mnr[0])
    #
    # n = int(mnr[1])

    r = 7

    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12],
    #           [13, 14, 15, 16],
    #           [19, 20, 21, 22],
    #           [25, 26, 27, 28]]
    matrix = [
        [1, 2, 3, 4],
        [7, 8, 9, 10],
        [13, 14, 15, 16],
        [19, 20, 21, 22],
        [25, 26, 27, 28]
    ]

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
