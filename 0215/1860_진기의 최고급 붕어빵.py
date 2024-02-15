import sys
sys.stdin = open('1860_input.txt')

def sell():
    global result
    bung = 0  # 만든 붕어빵 개수
    cnt = 0   # 판 붕어빵 개수

    for i in range(1, 11112):
        print(arr)
        if i % K == 0:
            bung += 1
        if arr:
            if arr[-1]-i < 0 or (arr[-1]-i >= 0 and bung-cnt < 1):
                result = 'Impossible'
                return
            elif arr[-1]-i >=0 and bung-cnt >=1:
                arr.pop()
                cnt +=1
        else:
            return


T = int(input())
for test_case in range(1, 5):
    # N손님수 M초 K붕어빵수
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True) # 정렬된 손님
    # print(arr) # [3, 4]
    result = 'Possible'

    sell()
    print(result)




    print(f'#{test_case}')
