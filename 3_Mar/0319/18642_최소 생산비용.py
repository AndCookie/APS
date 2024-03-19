import sys
sys.stdin = open('18642_input.txt')

def DFS(line, price):
    global result
    if result < price:
        return
    if line == n:
        if result > price:
            result = price

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(line+1, price + arr[line][i])
            visited[i] = False


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = float('inf')

    visited = [False] * n
    DFS(0, 0)

    print(f'#{test_case} {result}')

