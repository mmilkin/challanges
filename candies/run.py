#!/bin/python3

import math
import os
import random
import re
import sys


MAP_KNOWN_COMBINATIONS = {}


def candies(n, arr):
    left_to_right = [0] * len(arr)
    right_to_left = [0] * len(arr)

    left_to_right[0] = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            left_to_right[i] = left_to_right[i - 1] + 1
        else:
            left_to_right[i] = 1

    total = left_to_right[-1]

    right_to_left[len(arr) - 1] = 1

    for i in range(len(arr) - 2, - 1, -1):
        if arr[i] > arr[i + 1]:
            right_to_left[i] = right_to_left[i + 1] + 1
        else:
            right_to_left[i] = 1

        total += max(right_to_left[i], left_to_right[i])

    return str(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
