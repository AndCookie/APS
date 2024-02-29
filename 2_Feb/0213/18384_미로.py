import sys
sys.stdin = open('18384_input.txt')

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 출발지점 2를 찾기
def search(i, j):
    stack = [(i,j)]
    maze[i][j] = 1
    while stack:
        i, j = stack.pop()
        for di, dj in move:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '2':
                    return 1
                elif maze[ni][nj] == '0':
                    stack.append((ni,nj))
                    maze[ni][nj] = '1'
    return 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # n 미로의 크기
    maze = [] # 미로
    [maze.append(list(input())) for _ in range(n)]
    # print(maze) # [['1', '3', '1', '0', '1'], ['1', '0', '1', '0', '1']... ]

    print(f'#{test_case}', end=' ')

    # 도착지점 3의 인덱스
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '3':
                print(search(i,j))
