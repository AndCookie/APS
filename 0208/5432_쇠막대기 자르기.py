import sys
sys.stdin = open('5432_input.txt')

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    print(arr)
    length = len(arr)
    my = [[] for _ in range(len(arr))]
    print(my)
    for i in range(1, length):
        if arr[i-1] == '(' and arr[i] == ')':
            my[0].append(arr[i-1])
            my[0].append(arr[i])
    print(my)
    print(f'#{test_case}')
