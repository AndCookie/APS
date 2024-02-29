import sys
sys.stdin = open('1974_input.txt')

T = int(input())

for test_case in range(1, T+1):
    my_arr = [input().split() for _ in range(9)]
    my_set = set(str(i) for i in range(1,10))
    # print(my_arr)
    # print(my_set)

    result = 0
    ans = 1 # 1: 중복X / 0: 중복O

    # 가로 탐색
    for i in range(0, 9):
        if my_set.difference(set(my_arr[i])):
            result +=1

    # 세로 탐색
    for z in zip(*my_arr):
        # print(list(z))
        if my_set.difference(set(z)):
            result += 1

    # 네모 탐색
    new_set = set()
    for k in range(0,9,3):
        for i in range(k,k+3):
            for j in range(k,k+3):
                new_set.add(my_arr[i][j])
        if my_set.difference(new_set):
            result += 1
    
    if result != 0:
        ans = 0

    print(f'#{test_case} {ans}')
