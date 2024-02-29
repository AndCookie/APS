import sys
sys.stdin = open('18060_input.txt')

T = int(input())

for test_case in range(1, T+1):
    my_arr = list(i for i in range(1,13))
    N, K = map(int, input().split())
    # print(my_arr) # [1,2,...12]
    # print(N, K) # 3 6

    result = 0
    for i in range(1, 1 << len(my_arr)):
        cnt = s = 0
        for j in range(len(my_arr)):
            if i & (1 << j):
                cnt += 1
                s += my_arr[j]

        if cnt == N and s == K:
            result += 1

    print(f'#{test_case} {result}')
