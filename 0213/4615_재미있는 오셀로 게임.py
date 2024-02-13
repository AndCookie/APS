import sys
sys.stdin = open('4615_input.txt')

move = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
color_change = {1: 2, 2: 1}


def game(x, y, color): # 1 2 1
    # 돌 놓은 곳
    board[y-1][x-1] = color # board[1][0]

    # 돌 놓은 곳의 상하좌우, 대각선
    for di, dj in move:
        ni, nj = y-1 + di, x-1 + dj # ni,nj 상하좌우 # 1+0 0+1
        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == color_change[color]: # 2
                if 0 <= ni+di < N and 0 <= nj+dj < N: # 1+0 1+1
                    if board[ni+di][nj+dj] == color: # 1
                        board[ni][nj] = color

T = int(input())
for test_case in range(1, T + 1):
    # N 보드길이 M 돌 놓는 횟수
    N, M = map(int, input().split())
    my_arr = []
    [my_arr.append(list(map(int, input().split()))) for i in range(M)]
    # print(my_arr) # [[1, 2, 1], [1, 1, 2] ...]

    board = [[0] * N for _ in range(N)]
    # print(board)

    # 기본 백/흑돌 깔기
    board[N//2][N//2] = board[N//2-1][N//2-1] = 2 # 백
    board[N//2][N//2-1] = board[N//2-1][N//2] = 1 # 흑
    # print(board)

    for m in my_arr:
        x, y, color = m[0], m[1], m[2] # 1 2 1
        game(x, y, color)

    print(board)