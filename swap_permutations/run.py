#!/bin/python3

import os
import sys


#
# Complete the swapPermutation function below.
#
def swap_permutation(number, swaps):
    #
    # Write your code here.
    #
    return None, None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = swap_permutation(n, k)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
