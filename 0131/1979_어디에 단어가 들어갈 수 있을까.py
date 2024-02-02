import sys
sys.stdin = open('1979_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    my_arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    # 0을 패딩하기
    # print(my_arr)
    N += 1

    # 가로, 세로로 연속한 1의 개수가 K인 것의 개수 구하기
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if my_arr[i][j]:
                cnt += 1
            else:    # my_arr[i][j] ==0
                if cnt == K:
                    ans += 1
                cnt = 0

        for k in range(N):
            if my_arr[k][i]:
                cnt += 1
            else:    # my_arr[k][i] ==0
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{test_case} {ans}')
