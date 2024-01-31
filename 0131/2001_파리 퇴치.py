import sys
sys.stdin = open('2001_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(my_arr)

    fly_cnt = []
    for r in range(N-M+1): # 0~5가 아님!
        for c in range(N-M+1):
            s = 0
            for m in range(M): # 0~2
                for n in range(M):
                    if 0<=r+m<N and 0<=c+n<N :
                        s += my_arr[r+m][c+n]
            fly_cnt.append(s)
    maxi = 0
    for f in fly_cnt :
        if maxi < f :
            maxi = f

    print(f'#{test_case} {maxi}')
