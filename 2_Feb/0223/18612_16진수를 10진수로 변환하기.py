import sys
sys.stdin = open('18612_input.txt')

T = int(input())
for test_case in range(1, T+1):
    hex = input()
    arr = ''
    for h in hex:
        dec = int(h, base=16) # 16진수 -> 10진수
        b = format(dec, 'b').zfill(4)  # 10진수 -> 2진수
        arr += b

    result = []
    for i in range(len(arr)//7+1):
        tmp = arr[i*7:(i+1)*7]     # 7개씩 끊기
        result.append(int(tmp, 2)) # 2진수 -> 10진수
    print(f'#{test_case}', end=' ')
    print(*result)

