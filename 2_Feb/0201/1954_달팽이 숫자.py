import sys
sys.stdin = open('1954_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    my_arr = [[0]*N for _ in range(N)]
    print(my_arr)

    result = 0

    print(f'#{test_case} {result}')