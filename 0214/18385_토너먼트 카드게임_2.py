import sys
sys.stdin = open('18385_input.txt')

def search(start, end):
    # 토너먼트 경기
    for i in range(start, end, 2):
        global cnt
        cnt += 1
        if i + 1 <= end-1:
            candid.append(arr[i])
            candid.append(arr[i+1])
            if arr[i] == 1 and arr[i + 1] == 3:
                candid.pop(-1)
            elif arr[i] == 3 and arr[i + 1] == 1:
                candid.pop(-2)
            elif arr[i] >= arr[i + 1]:  # 비기는 경우 포함
                candid.pop(-1)
            elif arr[i] < arr[i + 1]:
                candid.pop(-2)
        else:
            candid.append(arr[i])


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # 인원수
    arr = list(map(int, input().split())) # 카드

    cnt = 0
    candid = []
    mid = len(arr) // 2
    search(0, mid)
    search(mid, len(arr))
    print(arr)
    print(candid)

    while cnt < n-1:
        mid = len(candid)//2
        candid.clear()
        search(0, mid)
        search(mid, mid*2)
        print(candid)

    # while True:
    #     mid = len(arr)//2
    #     left()
    #     right()
    #     arr = winner
    #     winner.clear()

    print(f'#{test_case}')
