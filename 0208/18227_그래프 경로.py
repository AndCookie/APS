import sys
sys.stdin = open('18227_input.txt')


result = []
def dfs(i, g):
    visited[i] = 1
    result.append(i)

    if i == g:
        return
    else:
        # i에 인접하면서 방문하지 않은 w가 있다면
        for w in adjl[i]:
            if visited[w] == 0:
                dfs(w, g)


T = int(input())
for test_case in range(1, T+1):
    # 정점의 개수 V=7 / 간선의 개수 E=8
    V, E = map(int, input().split())

    # 경로 저장
    arr = []
    for _ in range(E):
        arr.append(list(map(int, input().split())))
    # print(arr)

    # 출발 및 도착 노드
    S, G = map(int, input().split())

    # 인접 리스트
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    # print(adjl)

    # visited 생성 및 초기화
    visited = [0] * (V + 1)
    dfs(S, G)

    if G in result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
