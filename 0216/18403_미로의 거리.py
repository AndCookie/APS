import sys
sys.stdin = open('18403_input.txt')
from collections import deque

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 도착지점 3을 찾기
def search(i, j):
    
    # 시작점 방문
    queue = deque([(i,j)])
    maze[i][j] = 1

    while queue:
        i, j = queue.popleft()

        for di, dj in move:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '3':
                    return maze[i][j] - 1
                elif maze[ni][nj] == '0':
                    queue.append((ni,nj))
                    maze[ni][nj] = maze[i][j] + 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # n 미로의 크기
    maze = [] # 미로
    [maze.append(list(input())) for _ in range(n)]
    # print(maze) # [['1', '3', '1', '0', '1'], ['1', '0', '1', '0', '1']... ]

    print(f'#{test_case}', end=' ')

    # 도착지점 2의 인덱스
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                print(search(i,j))
                # print(maze)