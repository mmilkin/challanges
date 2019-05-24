#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the unboundedKnapsack function below.
def unbounded_knapsack(target, arr):
    buckets = [0 for _ in range(target)]

    # remove multiples from arr
    for number in sorted(arr):
        mult = target // number
        data = []
        value = 0
        for _ in range(1, mult + 1):
            data += [number]
            value += number

            for index in range(len(buckets), 0, -1):
                if (index + value) <= target and buckets[index - 1]:
                    buckets[index - 1 + value] = 1

                if index == 1:
                    pass

                if index == value:
                    buckets[index - 1] = 1

    for i in range(len(buckets), 0, -1):
        if buckets[i - 1]:
            return i
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    nk = input().split()

    n = int(nk[0])

    target = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = unbounded_knapsack(target, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
