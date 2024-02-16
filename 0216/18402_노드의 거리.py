import sys
sys.stdin = open('18402_input.txt')


def bfs(s, N, G):  # 시작정점s, 노드개수N, 마지막정점G
    q = []  # 큐 생성
    visited = [0] * (N + 1)  # visited 생성 및 초기화
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 인큐 포시

    while q:  # 처리 안된 정점이 남아있으면
        t = q.pop(0)  # 처리할 정점 디큐
        if t == G:
            return visited[t] - 1  # 시작정점이 1이므로 간선 개수 계산을 위해 -1

        for w in adjl[t]:  # t의 인접 정점이
            if visited[w] == 0:  # 인큐되지 않았으면 (방문한 적 없으면)
                q.append(w)
                visited[w] = visited[t] + 1

    return 0  # G까지의 경로가 없는 경우


T = int(input())
for test_case in range(1, T + 1):
    # 정점의 개수 V / 간선의 개수 E
    V, E = map(int, input().split())

    # 인접 리스트
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)

    # 출발노드 S / 도착노드 G
    S, G = map(int, input().split())

    print(f'#{test_case} {bfs(S, V, G)}')
