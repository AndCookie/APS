import sys
sys.stdin = open('1961_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(my_arr)

    arr_90 =[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][(N-1)-j] = my_arr[j][i]
    # print(arr_90)

    arr_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[i][(N - 1) - j] = arr_90[j][i]
    # print(arr_180)

    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[i][(N - 1) - j] = arr_180[j][i]
    # print(arr_270)

    print(f'#{test_case}')
    for i in range(N) :
        print(*arr_90[i], ' ', *arr_180[i], ' ', *arr_270[i], sep="")