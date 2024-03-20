import sys
sys.stdin = open('20642_input.txt')
from collections import deque
# '+1', '-1', '*2', '-10'

def BFS(start):
    queue = deque([start])

    while queue :
        now = queue.popleft()

        for calc in [now+1, now-1, now*2, now-10]:
            if calc == m:
                print(f'#{test_case}', visited[now] + 1)
                return
            if 0 < calc <= 1000000 and visited[calc] == 0:
                queue.append(calc)
                visited[calc] = visited[now] +1


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001 
    BFS(n)

