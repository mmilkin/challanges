#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return [i+1 for i in range(n)]

    if n % k != 0 and (n/k) % 2 != 0:
        return [-1]

    items = [-1] * n
    number = 1
    index = 0

    while index < (n - k):
        for item_bucket in range(k):
            items[index + item_bucket] = number + k + item_bucket
            items[index + k + item_bucket] = number + item_bucket
        number += (2 * k)
        index += (2 * k)

    return items

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
