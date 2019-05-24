#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.
def almostSorted(arr):
    out_of_order_indx = get_out_of_order(arr)
    sort = sorted(arr)
    if not out_of_order_indx:
        return 'yes'

    swap = can_swap(out_of_order_indx, arr, sort)
    if swap:
        return 'yes\nswap %s %s' % (swap[0] + 1, swap[1] + 1)

    reverse = can_reverse(out_of_order_indx, arr, sort)
    if reverse:
        return 'yes\nreverse %s %s' % (reverse[0] + 1, reverse[1] + 1)

    return 'no'


# 1 5 8 7 6 10
# 8 7 6 5 20
def can_reverse(indx, arr, sort):
    if indx < 1:
        return None

    differences = []

    for i in range(len(arr)):
        if arr[i] != sort[i]:
            differences.append(i)
    start = arr[:differences[0]]
    if differences[0] == 0:
        sorted_middle = arr[differences[-1]:: -1]
    else:
        sorted_middle = arr[differences[-1]: differences[0] - 1: -1]
    end = arr[differences[-1] + 1:]
    new_arr = start + sorted_middle + end
    if get_out_of_order(new_arr):
        return None

    return differences[0], differences[-1]


# 1 20 33 5 44
# 23 21 30 33 50
def can_swap(pivot, arr, sort):
    differences = []

    for i in range(len(arr)):
        if arr[i] != sort[i]:
            differences.append(i)

    if len(differences) == 2:
        return tuple(differences)

    return None


def get_out_of_order(arr):
    previous = arr[0]
    out_of_order_indx = None
    for indx in range(len(arr)):
        if arr[indx] < previous:
            out_of_order_indx = indx
            break
        previous = arr[indx]
    return out_of_order_indx


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))
