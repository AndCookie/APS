import sys
sys.stdin = open('1227_input.txt')
from collections import deque

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# 도착지점 3을 찾기
def search(i, j):
    # 시작점 방문
    queue = deque([(i, j)])
    maze[i][j] = 1

    while queue:
        i, j = queue.popleft()

        for di, dj in move:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < 100 and 0 <= nj < 100:
                if maze[ni][nj] == '3':
                    return 1
                elif maze[ni][nj] == '0':
                    queue.append((ni, nj))
                    maze[ni][nj] = 1
    return 0


for test_case in range(1, 11):
    n = int(input())
    maze = [list(input()) for _ in range(100)]
    # print(maze) # [['1', '3', '1', '0', '1'], ['1', '0', '1', '0', '1']... ]

    print(f'#{test_case}', end=' ')

    # 출발지점 2의 인덱스
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                print(search(i, j))
                # print(maze)
