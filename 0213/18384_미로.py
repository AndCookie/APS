import sys
sys.stdin = open('18384_input.txt')

# 출발지점 2를 찾기
def search(i, j):
    result = 0
    while True:
        cnt = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '1':
                    cnt += 1
                    # print(cnt)
                    continue
                elif maze[ni][nj] == '2':
                    return 1
                elif maze[ni][nj] == '0':
                    i = ni
                    j = nj
                    maze[ni][nj] = 1
                    cnt = 0
                    # print()
                    break
            else:
                cnt +=1
        if cnt >= 3:
            return 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # n 미로의 크기
    maze = [] # 미로
    [maze.append(list(input())) for _ in range(n)]
    # print(maze) # [['1', '3', '1', '0', '1'], ['1', '0', '1', '0', '1']... ]

    # 도착지점 3의 인덱스
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '3':
                ans = search(i, j)

    print(f'#{test_case} {ans}')
