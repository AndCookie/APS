import sys
sys.stdin = open('19606_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    di = [1, 1, -1, -1, 2, 2, -2, -2]
    dj = [-1, 1, -1, 1, -2, 2, -2, 2]

    result = arr[N//2][N//2]
    for k in range(8):
        ni = 2 + di[k]
        nj = 2 + dj[k]
        result += arr[ni][nj]

    print(f'#{test_case} {result}')
