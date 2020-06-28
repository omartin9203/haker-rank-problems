
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import *

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    X = [];
    for i in range(len(s)):
        X.extend(s[i])
    res = 81
    for P in permutations(range(1, 10)):
        if sum(P[0:3]) == 15\
                and sum(P[3:6]) == 15 and sum(P[0::3]) == 15\
                and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15\
                and (P[2] + P[4] + P[6] == 15):
            res = min(res, sum(abs(P[i] - X[i]) for i in range(0, 9)))
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [
        [4, 8, 2],
        [4, 5, 7],
        [6, 1, 6]
    ]

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()