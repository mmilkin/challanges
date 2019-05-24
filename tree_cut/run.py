#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

from collections import namedtuple, deque, defaultdict

Node = namedtuple('Node', ['index', 'value', 'children'], rename=True)

TREE_SUM = defaultdict(lambda: 0)


def build_tree(data, edges):
    nodes = [Node(index=index + 1, value=val, children=list()) for index, val in enumerate(data)]

    q = deque([nodes[0]])

    while q:
        node = q.popleft()
        edges_to = [edge for edge in edges if edge[0] == node.index or edge[1] == node.index]
        for edge in edges_to:
            index = edge[1] if edge[0] == node.index else edge[0]
            child = nodes[index - 1]
            node.children.append(child)
            edges.remove(edge)
            q.append(child)
    return nodes[0]


def fill_sum(head):
    stack = deque([head])
    children_order = [head]
    while stack:
        node = stack.pop()
        stack.extendleft(node.children)
        children_order.extend(node.children)

    while children_order:
        node = children_order.pop()
        TREE_SUM[node.index] = sum([TREE_SUM[child.index] for child in node.children]) + node.value

    return head


def cut_the_tree(data, edges):
    tree = build_tree(data, edges)
    fill_sum(tree)
    min_diff = None
    queue = deque([tree])
    full_tree_value = TREE_SUM[tree.index]

    while queue:
        node = queue.popleft()
        branch_1 = TREE_SUM[node.index]
        branch_2 = full_tree_value - branch_1

        current_diff = int(abs(branch_2 - branch_1))
        if min_diff is None:
            min_diff = TREE_SUM[node.index]
        elif current_diff < min_diff:
            min_diff = current_diff
        queue.extend((child for child in node.children))

    return min_diff
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cut_the_tree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
