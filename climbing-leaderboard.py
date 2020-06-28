#!/bin/python3


def binary_search(scores, score, low, high):
    if high >= low:
        mid = (high + low) // 2
        if scores[mid] == score:
            return mid + 1
        elif scores[mid] < score:
            return binary_search(scores, score, low, mid - 1)
        else:
            return binary_search(scores, score, mid + 1, high)
    else:
        if high >= 0:
            return high + 2
        else: return 1


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    pos = 1
    prev = scores[0]
    new_scores = [scores[0]]
    for x in scores[1:]:
        if not(x == prev):
            new_scores.append(x)
        prev = x
    return [binary_search(new_scores, x, 0, len(new_scores) - 1) for x in alice]


if __name__ == '__main__':
    scores_count = 6

    scores = list(map(int, '100 100 50 40 40 20 10'.split()))

    alice_count = 5

    alice = list(map(int, '5 25 50 120'.split()))

    result = climbingLeaderboard(scores, alice)
    print(result)