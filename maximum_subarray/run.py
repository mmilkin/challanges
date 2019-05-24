#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    if not arr:
        return 0, 0

    current_sum = arr[0]
    total_sum = 0
    pointer = start = 0
    end = 0

    # max_sum = 2
    # [2 ,10, -14, 9, 1]
    # max_sum = 2 or 10 + 2
    # sum = 10
    # array 0 - 2
    # ---
    # sum = -14 or -2
    # sum = 10
    # start = 1
    sorted_arr = sorted(arr)
    max_sum = sorted_arr[0]
    for element in sorted_arr[1:]:
        max_sum = max(max_sum + element, element)

    for i, element in enumerate(arr[1:]):
        current_sum = max(current_sum + element, element)
        total_sum = max(total_sum, current_sum)

        if current_sum < 0:
            # If we encounter an element that makes us go negative find move the left point
            start += 1
        elif total_sum == current_sum:
            # If we find equality mark index
            pointer = start
            end = i + 1

    return '%s %s' % (sum(arr[pointer: end + 1]), max_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
