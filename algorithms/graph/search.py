from collections import deque

from algorithms.collections.graph import Graph


def bfs(graph: Graph, root):
    dq = deque([root])
    visited = set()
    scanned = []
    while len(dq) > 0:
        node = dq.pop()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            if child in visited:
                continue
            dq.appendleft(child)
        scanned.append(node)
    return scanned


def dfs(graph: Graph, root):
    dq = deque([root])
    visited = set()
    scanned = []
    while len(dq) > 0:
        node = dq.pop()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            if child in visited:
                continue
            dq.append(child)
        scanned.append(node)
    return scanned
