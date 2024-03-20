import sys
sys.stdin = open('18459_input.txt')
from collections import deque

def BFS(start):
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        path.append(now)

        for to in graph[now]:
            if visited[to]:
                continue
            visited[to] = 1
            queue.append(to)

T = 1
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    for idx in range(0, len(arr)-1, 2):
        parent = arr[idx]
        child = arr[idx+1]
        graph[parent].append(child)
    # print(graph) # [[], [2, 3], [4, 5], [7], [6], [6], [7], []]

    path = []
    visited = [0] * (V+1)
    BFS(1)
    print(f'#{test_case}', *path)

