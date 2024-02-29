import sys
sys.stdin = open('4615_input.txt')

def game(x, y, color): # 1 2 1
    move = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    # 돌 놓은 곳
    board[x][y] = color # board[1][0]

    # 돌 놓은 곳의 상하좌우, 대각선
    for di, dj in move:
        count = 1
        while 0 <= x + di*count < N and 0 <= y + dj*count < N:
            ni, nj = x + di*count, y + dj*count  # ni,nj 상하좌우 # 1+0 0+1
            if board[ni][nj] == 0:
                break
            elif board[ni][nj] == color: # 2
                for k in range(1, count):
                    board[x + di * k][y + dj * k] = color
                break
            count += 1

T = int(input())
for test_case in range(1, T + 1):
    # N 보드길이 M 돌 놓는 횟수
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    # 기본 백/흑돌 깔기
    board[N//2][N//2] = board[N//2-1][N//2-1] = 2 # 백
    board[N//2][N//2-1] = board[N//2-1][N//2] = 1 # 흑
    # print(board)

    for _ in range(M):
        x, y, color = map(int, input().split())
        game(y-1, x-1, color)

    black = 0
    white = 0
    for i in board:
        for j in i:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1
    print(f'#{test_case} {black} {white}')