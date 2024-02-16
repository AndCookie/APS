import sys
sys.stdin = open('18459_input.txt')


q = []
result  = []
def bfs(start, n): # 시작정점s, 노드개수n
    visited[start] = 1
    q.append(start)

    while q:
        t = q.pop(0)
        result.append(t)
        # t에 인접하면서 방문하지 않은 w가 있다면
        for w in adjl[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1 + visited[t]
    # print(visited)


# 정점의 개수 V=7 / 간선의 개수 E=8
V, E = map(int, input().split())

# 경로 저장
arr = list(map(int, input().split()))

# 인접 리스트
adjl = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for a in adjl:
    a.sort()
# print(adjl)

# visited 생성 및 초기화
visited = [0] * (V + 1)
print('#1', end=" ")
bfs(1, V)
print(*result, sep=" ")
