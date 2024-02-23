import sys
sys.stdin = open('18613_input.txt')

pattern = {'001101':0, '010011':1, '111011':2, '110001':3, '100011':4,
           '110111':5, '001011':6, '111101':7, '011001':8, '101111':9 }

T = int(input())
for test_case in range(1, T+1):
    hex = input().strip()
    arr = ''
    for h in hex:
        dec = int(h, base=16)  # 16진수 -> 10진수
        b = format(dec, 'b').zfill(4)  # 10진수 -> 2진수
        arr += b
    # print(arr)

    result = []
    tmp = arr.strip('0')
    length = (len(tmp)//6+1)*6    # 길이는 6의배수
    adjusted = tmp.zfill(length)

    for i in range(length//6):
        six = adjusted[i*6:(i+1)*6]
        result.append(pattern[six])
    print(f'#{test_case}', end=' ')
    print(*result)

