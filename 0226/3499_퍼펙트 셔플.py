import sys
sys.stdin = open('3499_input.txt')


def loop():
    a = 0
    b = (n+1) // 2

    for i in range(n):
        if i%2 == 0:
            print(my_arr[a], end = ' ')
            a += 1
        else:
            print(my_arr[b], end=' ')
            b += 1


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    my_arr = list(input().split())

    print(f'#{test_case}', end=' ')
    loop()
    print()

