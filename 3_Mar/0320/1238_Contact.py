import sys
sys.stdin = open('1238_input.txt')
from collections import deque

def BFS(start):
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = deque([start])
    visited[start] = 1

    while queue:
        now = queue.popleft()

        # 갈 수 있는 곳을 체크
        for to in graph[now]:	
            # 이미 방문했다면 pass
            if visited[to]:
                continue
            queue.append(to)
            visited[to] = visited[now] + 1


T = 10
for test_case in range(1, T+1):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    
    graph = [[] for _ in range(101)]
    for i in range(0, length-1, 2):
        parent, child = arr[i], arr[i+1]
        graph[parent].append(child)
    # print(graph)
    
    visited = [0] * 101
    BFS(start)

    candidate = []
    for idx in range(len(visited)):
        if visited[idx] == max(visited):
            candidate.append(idx)

    print(f'#{test_case}', max(candidate))

