import sys
sys.stdin = open('1219_input.txt')

result = []
def dfs(i):
    visited[i] = 1
    result.append(i)

    if i == 99:
        return
    else:
        # i에 인접하면서 방문하지 않은 w가 있다면
        for w in adjl[i]:
            if visited[w] == 0:
                dfs(w)


for test_case in range(1, 11):
    T, E = map(int, input().split())

    # 경로 저장 / 인접 리스트
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(99)]
    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjl[n1].append(n2)
    # print(adjl)

    # visited 생성 및 초기화
    visited = [0] * 100
    dfs(0)

    if 99 in result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
    # 초기화
    result = []
