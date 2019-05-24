#!/bin/python3

import os
import sys
from collections import deque, defaultdict


def rust_graph(village_roads, start, cities):
    if not village_roads:
        return {}

    shortest_distance = defaultdict(set)
    shortest_distance[start] = -1
    q = deque([(1, n) for n in village_roads[start]])
    while q:
        node = q.pop()
        if len(shortest_distance) == cities:
            break
        if node[1] not in shortest_distance:
            shortest_distance[node[1]] = node[0]
            q.extendleft([(1 + node[0], child) for child in village_roads.get(node[1], [])])
    shortest_distance.pop(start, None)
    return shortest_distance


def rust_murdered(cities, roads, rust):
    nodes = set((z for z in range(1, cities + 1)))
    village_roads = {}
    for node in nodes:
        village_roads[node] = nodes.difference({node})

    for road in roads:
        village_roads[road[0]].remove(road[1])
        village_roads[road[1]].remove(road[0])

    distance_map = rust_graph(village_roads, rust, cities)
    return (i[1] for i in sorted(distance_map.items()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        rds = []

        for _ in range(m):
            rds.append(list(map(int, input().rstrip().split())))

        r = int(input())

        result = rust_murdered(n, rds, r)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
