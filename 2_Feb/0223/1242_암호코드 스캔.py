import sys
sys.stdin = open('1242_input.txt')

my_dict= {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
          '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }

T = int(input())
for test_case in range(1, T+1):
    # 배열의 세로N, 가로M
    N, M = map(int, input().split())
    code = ''
    for _ in range(N):
        arr = input().strip('0')
        if arr:
            code = arr.zfill(56)

    check = 0
    result = 0
    for i in range(1, 9):
        tmp = my_dict[code[7*(i-1) : 7*i]]
        result += tmp
        if i == 8:
            check += tmp
        else:
            if i % 2:
                check += tmp * 3
            else:
                check += tmp

    if check % 10:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {result}")
