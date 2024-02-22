import sys
sys.stdin = open('18593_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = ''
    for _ in range(N):
        arr += input().strip()
    print(f'#{test_case}', end=' ')
    for i in range(0, N*10, 7):
        string = arr[i:i + 7]
        result = 0
        for j in range(7):
            result += int(string[6-j]) * pow(2, j)
        print(result, end=' ')
