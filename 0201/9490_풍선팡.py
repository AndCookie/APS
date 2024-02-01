import sys
sys.stdin = open('9490_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(my_arr)

    flower_cnt = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for r in range(N):  # 0~2
        for c in range(M): # 0~4
            result = my_arr[r][c]
            # result의 값만큼 상하좌우 터지도록 설정
            for i in range(1, result+1):
                for k in range(4): # 0~3
                    ni = r + di[k]*i
                    nj = c + dj[k]*i
                    if 0 <= ni < N and 0 <= nj < M:
                        result += my_arr[ni][nj]
            flower_cnt.append(result)

    maxi = 0
    for f in flower_cnt:
        if maxi < f:
            maxi = f

    print(f'#{test_case} {maxi}')