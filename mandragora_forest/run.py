#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the mandragora function below.
def mandragora(h):
    pass
    # [ 3 2 2 ]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        h = list(map(int, input().rstrip().split()))

        result = mandragora(h)

        fptr.write(str(result) + '\n')

    fptr.close()
