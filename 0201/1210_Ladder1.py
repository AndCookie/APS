import sys
sys.stdin = open('1210_input.txt')

for _ in range(1, 11):
    test_case = input()
    my_arr = [list(input().split()) for _ in range(100)]
    # print(my_arr)

    r = 98
    c = my_arr[-1].index('2') # 57
    # print(my_arr[r][c])

    while r != 0:
        my_arr[r][c] = '0'
        if 0 <= c-1 and my_arr[r][c-1] == '1':
            c -= 1
        elif 100 > c+1 and my_arr[r][c+1] == '1':
            c += 1
        else:
            r -= 1

    print(f'#{test_case} {c}')
