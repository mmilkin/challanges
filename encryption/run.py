#!/bin/python3

import math
import os
import random
import re
import sys

from math import sqrt, ceil


# Complete the encryption function below.
def encryption(phrase):
    assert phrase is not None
    phrase = re.sub(r'\s*', '', phrase)

    L = len(phrase)
    sqr_L = sqrt(L)
    top = int(ceil(sqr_L))
    bottom = int(sqr_L)

    #bottom =< R =< C =< top
    proposed_columns = len(phrase[:top])

    if proposed_columns > top and top+1 <= bottom:
        proposed_columns = len(phrase[:top + 1])

    sets = [phrase[n: n + proposed_columns] for n in range(0, L, proposed_columns)]
    end_len = len(sets[-1])
    if len(sets[-1]) < proposed_columns:
        sets[-1] += " " * (proposed_columns - end_len)

    # import pdb; pdb.set_trace()
    return " ".join("".join(word).strip() for word in zip(*sets))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
