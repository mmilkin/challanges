#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

from collections import defaultdict

def get_cost(nodes, from_node, to_node):
    # Print your answer within the function and return nothing
    train_map = {}
    train_cost = defaultdict(sys.maxsize)

    for item in nodes:
        f, t, c = item


    pass

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    get_cost(g_nodes, g_from, g_to, g_weight)
