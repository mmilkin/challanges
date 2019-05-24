#!/bin/python3

import math
import os
import random
import re
import sys


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def is_equal(a, b):
    return b in a.upper()


@Memoize
def compute_part(a, b):
    if len(a) < len(b):
        return False

    for indx, letter in enumerate(a):
        if letter.islower():
            continue
        else:
            starts = [m.start() for m in re.finditer(letter, b)]
            for start in starts:
                if is_equal(a[:indx + 1], b[:start + 1]):
                    if compute_part(a[indx+1:], b[start+1:]):
                        return True
            return False
    return True


for (int i = 0; i < s1.length(); i++){
    for (int j = 0; j <= s2.length(); j++)
    {
        if (dp[i][j])
        {
            if(j < s2.length() and (upcase(s1[i]) == s2[j]))
                dp[i + 1][j + 1] = true;
            if(!isUpcase(s1[i]))
                dp[i + 1][j] = true;
        }
    }
}


# Complete the abbreviation function below.
def abbreviation(a, b):
    if compute_part(a, b):
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
