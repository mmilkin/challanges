#!/bin/python3

import os
from itertools import product, chain
from collections import deque

def computer_game(a, b):
    edges = compute_graph(a, b)
    print "created Graph"
    return max_to_remove(edges)


def compute_graph(a, b):
    edges = {}
    for i in chain(a, b):
        edges[i] = set()

    print "ZZZZZ"
    x = list(product(a, b))
    z = len(x)
    for i, item in enumerate(x):
        first, second = item
        print "processing %s out of %s" % (i, z)
        if common_factor(first, second):
            edges[first].add(second)
            edges[second].add(first)
    return edges


def max_to_remove(graph):
    item = item_to_remove(graph)
    pairs_to_remove = 0
    while item:
        pairs_to_remove += 1

        for edge in graph.items():
            if item[0] in edge[1]:
                edge[1].remove(item[0])
            if item[1] in edge[1]:
                edge[1].remove(item[1])

        del graph[item[0]]
        del graph[item[1]]

        item = item_to_remove(graph)
    return pairs_to_remove


def item_to_remove(graph):
    min_to_remove = None
    for key, value in graph.items():
        if value:
            if min_to_remove is None:
                min_to_remove = (key, value)
            elif min_to_remove and len(min_to_remove[1]) > len(value):
                min_to_remove = (key, value)

    if min_to_remove is None:
        return None

    key2 = None
    for potential_key in min_to_remove[1]:
        if key2 is None:
            key2 = potential_key
        elif len(graph[key2]) > len(graph[potential_key]):
            key2 = potential_key

    return min_to_remove[0], key2


def common_factor(first, second):
    if gcd(first, second) == 1:
        return False
    return True


# class Memoize:
#     def __init__(self, fn):
#         self.fn = fn
#         self.memo = {}
#
#     def __call__(self, *args):
#         if args not in self.memo:
#             self.memo[args] = self.fn(*args)
#         return self.memo[args]

MEMO = {}

def gcd(a_, b_):
    deque = [(a_, b_)]

    while deque:
        item = deque[-1]
        X = MEMO

        if item in MEMO:
            result = MEMO[item]
            while deque:
                item = deque.pop()
                MEMO[item] = result
            return result

        a, b = item
        if a == 0 or b == 0:
            MEMO[(a, b)] = 0

        if a == b:
            MEMO[(a, b)] = a
            continue

        # a is greater
        if a > b:
            deque.append((a - b, b))
            continue

        deque.append((a, b - a))

    return MEMO[(a_, b_)]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = computer_game(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
