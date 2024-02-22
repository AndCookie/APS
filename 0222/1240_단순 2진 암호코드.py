import sys
sys.stdin = open('1240_input.txt')

my_dict= {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
          '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }

def verification():
    global result
    global verify
    cnt = 0
    for i in range(0, M, 7):
        string = arr[i:i + 7]
        print(string)
        if string != '0000000':
            result += my_dict[string]
            if cnt%2 == 0:
                verify += int(string[cnt]) * pow(2, 6-cnt) * 3
            else:
                verify += int(string[cnt]) * pow(2, 6-cnt)
            cnt += 1
        else:
            continue
    if verify % 10 == 0:
        return result
    else:
        return 0


T = int(input())
for test_case in range(1, T+1):
    # 배열의 세로N, 가로M
    N, M = map(int, input().split())
    print(f'#{test_case}', end=' ')

    for _ in range(N):
        arr = input()
        result = 0
        verify = 0
        if arr != '0'*M:
            print(verification())

