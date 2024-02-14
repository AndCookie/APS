import sys
sys.stdin = open('18385_input.txt')


def game(arr, a, b):
    if arr[a] - arr[b] == 1:
        return a
    elif arr[a] - arr[b] == -1:
        return b
    elif arr[a] == arr[b]:
        return a
    else:
        if arr[a] == 1:
            return a
        return b


def candid(arr, start, end):
    if end - start <= 1:
        return game(arr, start, end)
    a = candid(arr, start, (start+end)//2)
    b = candid(arr, (start+end)//2+1, end)
    return game(arr, a, b)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) # 인원수
    arr = list(map(int, input().split())) # 카드
    ans = candid(arr, 0, n-1)
    print(f'#{test_case} {ans+1}')
