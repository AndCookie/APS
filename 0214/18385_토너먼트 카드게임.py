import sys
sys.stdin = open('18385_input.txt')

def left():
    # 왼
    for i in range(0, mid, 2):
        if i + 1 <= mid - 1:
            if arr[i] == 1 and arr[i + 1] == 3:
                winner.append(arr[i])
            elif arr[i] == 3 and arr[i + 1] == 1:
                winner.append(arr[i + 1])
            elif arr[i] >= arr[i + 1]:  # 비기는 경우 포함
                winner.append(arr[i])
            elif arr[i] < arr[i + 1]:
                winner.append(arr[i + 1])
        else:
            winner.append(arr[i])

def right():
    # 오
    for i in range(mid, len(arr), 2):
        if i + 1 <= n - 1:
            if arr[i] == 1 and arr[i + 1] == 3:
                winner.append(arr[i])
            elif arr[i] == 3 and arr[i + 1] == 1:
                winner.append(arr[i + 1])
            elif arr[i] >= arr[i + 1]:  # 비기는 경우 포함
                winner.append(arr[i])
            elif arr[i] < arr[i + 1]:
                winner.append(arr[i + 1])
        else:
            winner.append(arr[i])


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # 인원수
    arr = list(map(int, input().split())) # 카드

    winner = []
    mid = len(arr) // 2
    left()
    right()


    # while True:
    #     mid = len(arr)//2
    #     left()
    #     right()
    #     arr = winner
    #     winner.clear()

    print(arr)
    print(winner)


    # while True:
    #     if len(winner)==1:
    #         break
    #     left()
    #     right()
    #
    # print(winner)


    print(f'#{test_case}')
