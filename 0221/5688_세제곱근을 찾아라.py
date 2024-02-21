import sys
sys.stdin = open('5688_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = round(pow(N, 1/3), 5)
    if result.is_integer():
        result = int(result)
    else:
        result = -1

    print(f'#{test_case} {result}')

