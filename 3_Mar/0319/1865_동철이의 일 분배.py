import sys
sys.stdin = open('1865_input.txt')


def DFS(work, perc):
    global result
    if perc <= result:
        return
    
    if work == n:
        result = max(result, perc)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(work+1, perc * (arr[work][i]/100))
            visited[i] = False

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    visited = [False] * n
    DFS(0, 1)
    print(f'#{test_case} {"{:.6f}".format(round(result*100, 7))}')

