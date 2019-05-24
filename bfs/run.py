#!/bin/python3

import os
from collections import deque, defaultdict


def bfs(nodes, edges, start):
    graph = build_graph(edges, nodes)
    queue = deque([(start, 6)])
    seen = {start}
    distances = defaultdict(lambda : -1)
    while queue:
        node = queue.popleft()
        links = graph.get(node[0])
        for link in links:
            if link not in seen:
                queue.append((link, node[1] + 6))
                seen.add(link)
                distances[link] = node[1]
    return [
        distances[i] for i in range(1, nodes + 1) if i != start
    ]


def build_graph(edges, nodes):
    graph = defaultdict(set)

    for i in range(1, nodes+1):
        graph[i].add(i)

    for edge in edges:
        graph.get(edge[0]).add(edge[1])
        graph.get(edge[1]).add(edge[0])
    return graph


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(tuple(map(int, input().rstrip().split())))

        start = int(input())

        result = bfs(n, edges, start)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
