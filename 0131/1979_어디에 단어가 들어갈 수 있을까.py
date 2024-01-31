import sys
sys.stdin = open('1979_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(my_arr)

    cnt = result = 0
    for r in range(N):
        for c in range(N):
            if 1 in my_arr[r]:
                cnt += 1
        if cnt == 3:
            row_sum = col_sum = 0
            if my_arr[r][c] == 1:
                for k in range(3):
                    if 0 <= c+k < N:
                        row_sum += my_arr[r][c+k]
                    if 0 <= r+k < N:
                        col_sum += my_arr[r+k][c]
            if row_sum == K:
                result += 1
            if col_sum == K:
                result += 1

    print(f'#{test_case} {result}')
