#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    # [ 7, 6, 3, 1]
    integers_map = {i: i for i in arr}
    seen = set()

    for i in arr:
        item = i - k

        item_considered = tuple(sorted((item, i)))
        if item_considered in seen:
            break

        if item in integers_map:
            seen.add(item_considered)

    print(len(seen))
    return seen


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
