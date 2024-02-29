import sys
sys.stdin = open('1238_input.txt')


def bfs(s):  # 시작정점s, 노드개수N
    q = []  # 큐 생성
    visited = [0] * (101)  # visited 생성 및 초기화
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 인큐 포시

    while q:  # 처리 안된 정점이 남아있으면
        t = q.pop(0)  # 처리할 정점 디큐

        for w in adjl[t]:  # t의 인접 정점이
            if visited[w] == 0:  # 인큐되지 않았으면 (방문한 적 없으면)
                q.append(w)
                visited[w] = visited[t] + 1

    maxi = 0
    idx = 0
    for i in range(101):
        if maxi <= visited[i]:
            maxi = visited[i]
            idx = i
    return idx


for test_case in range(1, 11):
    length, start = map(int, input().split())

    # 경로 저장 / 인접 리스트
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(101)]
    for i in range(length//2):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjl[n1].append(n2)

    print(f'#{test_case} {bfs(start)}')
