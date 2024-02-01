import sys
sys.stdin = open('18123_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sub = total = 0;
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sub += abs(arr[ni][nj] - arr[i][j])
                    # print(sub)
    total += sub

    print(f'#{test_case} {total}')
