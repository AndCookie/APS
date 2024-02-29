import sys
sys.stdin = open('1232_input.txt')


def cal(num):
    if arr[num].isdecimal():
        return int(arr[num])
    elif arr[num] == '+':
        return cal(left[num]) + cal(right[num])
    elif arr[num] == '-':
        return cal(left[num]) - cal(right[num])
    elif arr[num] == '*':
        return cal(left[num]) * cal(right[num])
    elif arr[num] == '/':
        return cal(left[num]) / cal(right[num])


for test_case in range(1, 11):
    N = int(input())
    arr = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        node, num, *children = input().split()
        node = int(node)
        children = list(map(int, children))
        arr[node] = num
        if children:
            for c in children:
                if left[node] == 0:
                    left[node] = c
                else:
                    right[node] = c
    result = cal(1)
    print(f'#{test_case} {int(result)}')

