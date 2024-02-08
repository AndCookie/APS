# DFS
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(i): # 시작i
    visited[i] = 1 # 방문표시
    print(i)       # 출력

    # i에 인접하면서 방문하지 않은 w가 있다면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


# 정점의 개수 V=7 / 간선의 개수 E=8
V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
# adjl[i][j] / i에 인접한 정점 번호
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    # 방향이 없는 경우에는 서로 연결시켜주는 코드 추가
    adjl[n2].append(n1)
# print(adjl)
# 1번에 인접한 것은 2,3 / 2번에 인접한 것은 1,4,5 / ... / 7번에 인접한 것은 6,3
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

# visited 생성 및 초기화
visited = [0]*(V+1)

dfs(1)

'''
출력값
1
2
4
6
5
7
3
'''