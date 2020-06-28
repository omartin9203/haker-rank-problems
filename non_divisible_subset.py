#!/bin/python3


def nonDivisibleSubset(K, s):
    n = len(s)
    reminer = [0 for i in range(K)]
    for i in range(n):
        reminer[s[i] % K] += 1
    if K % 2 == 0:
        reminer[K // 2] = min(reminer[K // 2], 1)
    res = min(reminer[0], 1)
    for i in range(1, (K // 2) + 1):
        res += max(reminer[i], reminer[K - i])
    return res


if __name__ == '__main__':
    n = 7
    k = 6
    # s = list(map(int, "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".split()))
    s = list(map(int, "19 10 12 10 24 25 22".split()))
    result = nonDivisibleSubset(k, s)
    print(result)