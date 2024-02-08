import sys
sys.stdin = open('18311_input.txt')

result = []
def dfs(i):
    visited[i] = 1
    result.append(i)

    # i에 인접하면서 방문하지 않은 w가 있다면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


# 정점의 개수 V=7 / 간선의 개수 E=8
V, E = map(int, input().split())

# 경로 저장 / 인접 리스트
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(adjl)

# visited 생성 및 초기화
visited = [0]*(V+1)
print('#1', end=" ")
dfs(1)
print(*result, sep="-")