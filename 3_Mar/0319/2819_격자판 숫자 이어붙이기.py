import sys
sys.stdin = open('2819_input.txt')

dx = [1,0,-1,0]
dy = [0,-1,0,1]
def dfs(x,y):
    if len(path)==7 :
        # print(path)
        answer.add(''.join(map(str, path)))
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<4 and 0<=ny<4:
            path.append(board[nx][ny])
            dfs(nx,ny)
            path.pop()

T = int(input())
for test_case in range(1, T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    answer = set()
    for r in range(4):
        for c in range(4):
            path = [board[r][c]]
            dfs(r,c)
    print(f'#{test_case} {len(answer)}')

