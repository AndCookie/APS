import sys
sys.stdin = open('18311_input.txt')


def DFS(start):
    for to in sorted(graph[start]):
        if visited[to]:
            continue
        visited[to] = 1
        path.append(str(to))
        DFS(to)

T = 1
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    for idx in range(0, len(arr)-1, 2):
        parent = arr[idx]
        child = arr[idx+1]
        graph[parent].append(child)
        graph[child].append(parent)
    
    path = []
    visited = [0] * (V+1)

    visited[1] = 1
    path.append('1')

    DFS(1)
    print(f'#{test_case} {"-".join(path)}')

