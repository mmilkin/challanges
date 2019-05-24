#!/bin/python3

import os


def print_function(data):
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write('\n'.join(data))
        fptr.write('\n')


def print_std_out(data):
    print(data)


# Complete the bomberMan function below.
def bomber_man(r, c, n, grid):
    rows = r
    cols = c

    grid = [
        list(row) for row in grid
    ]

    if n % 2 == 0:
        n = 2

    if n > 3:
        n = n % 4 + 4

    if n > 0:
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == 'O':
                   grid[row][col] = 1

    for i in range(1, n):
        if i % 2 != 0:
            for row in range(0, rows):
                for col in range(0, cols):
                    if grid[row][col] != '.':
                        grid[row][col] += 1
                    else:
                        grid[row][col] = 0
        else:
            for row in range(0, rows):
                for col in range(0, cols):
                    if explode(row, col, grid):
                        grid = flood_fill(row, col, grid)
                    elif grid[row][col] != '.':
                        grid[row][col] += 1

    return grid


def explode(row, col, grid):
    value = grid[row][col]
    return value != '.' and value >= 2


def flood_fill(row, col, grid):
    queue = [(row, col)]
    max_row = len(grid)
    max_col= len(grid[0])

    while queue:
        item = queue.pop(0)
        row, col = item
        if row >= max_row or col >= max_col:
            continue

        grid[row][col] = '.'
        if col - 1 >= 0:
            if explode(row, col -1, grid):
                queue.append((row, col - 1))
            grid[row][col - 1] = '.'
        if row - 1 >= 0:
            if explode(row - 1, col, grid):
                queue.append((row - 1, col))
            grid[row - 1][col] = '.'
        if row + 1 < max_row:
            if explode(row + 1, col, grid):
                queue.append((row + 1, col))
            grid[row + 1][col] = '.'
        if col + 1 < max_col:
            if explode(row, col + 1, grid):
                queue.append((row, col + 1))
            grid[row][col + 1] = '.'

    return grid


def run(print_fn):
    rcn = input()
    rcn = rcn.split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = [''.join(
        [item if item == '.' else 'O' for item in row]
    ) for row in bomber_man(r, c, n, grid)]

    print_fn(result)


if __name__ == '__main__':
    run(print_function)
    run(print_std_out)
