#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


# Complete the gridlandMetro function below.
def gridland_metro(n, m, k, tracks):
    # grid = make_grid(n, m, tracks)
    # total = 0
    # for column in grid:
    #     total += sum(column)
    # return total
    track_area = consolidate_trains(tracks)
    total_area = n * m
    return total_area - track_area


def consolidate_trains(tracks):
    grid = defaultdict(list)
    for track in tracks:
        grid[track[0]].append((track[1] - 1, track[2]))

    sum_lines = 0
    for trains in grid.values():
        sum_lines += consolidate_row(sorted(trains))

    return sum_lines


def consolidate_row(track):
    subtract = 0
    previous_range_end = 0
    for line in track:
        start = line[0]
        end = line[1]

        if end <= previous_range_end:
            continue

        if previous_range_end > start:
            subtract += end - previous_range_end
        else:
            subtract += end - start

        previous_range_end = end

    return subtract


def make_grid(n, m, tracks):
    grid = []
    for i in range(n):
        grid.append([1]*m)

    for track in tracks:
        column = grid[track[0] - 1]
        for i in range(track[1] - 1, track[2]):
            column[i] = 0
        grid[track[0] - 1] = column

    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridland_metro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
