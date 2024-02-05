import sys
sys.stdin = open('18222_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    my_arr = [input() for _ in range(N)]
    # print(my_arr)

    result = ''
    mid = []
    new_arr = []
    for i in range(0, N):
        for j in range(0, N-M+1):
            mid.append(my_arr[i][j])
            if my_arr[i][j:j+M] == my_arr[i][j+M-1::-1]:
                result = my_arr[i][j:j+M]
            # print(my_arr[i][j])
    print(mid)
    new_arr.append(mid)
    print(new_arr)

    if not result :
        for i in range(0, N):
            for j in range(0, N - M + 1):
                if mid[i][j:j + M] == mid[i][j + M - 1::-1]:
                    result = mid[i][j:j + M]

    print(f'#{test_case} {result}')
