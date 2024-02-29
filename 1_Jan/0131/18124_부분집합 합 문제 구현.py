import sys
sys.stdin = open('18124_input.txt')

T = int(input())

for test_case in range(1, T+1):
    my_arr = list(map(int, input().split()))
    # print(my_arr)
    N = len(my_arr)

    result = 0
    for i in range(1, 1<<N):
        s = 0
        for j in range(N):
            if i&(1<<j):
                s += my_arr[j]
        if s == 0:
            result=1

    print(f'#{test_case} {result}')
