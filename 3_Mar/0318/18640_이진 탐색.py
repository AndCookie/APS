import sys
sys.stdin = open('18640_input.txt')

def binarySearch(arr, target, left, right):
    global cnt
    flag = 0

    while left <= right :
        mid = (left + right)//2

        if arr[mid] == target :
            cnt += 1
            return

        elif arr[mid] > target:
            if flag == -1:
                break
            right = mid - 1
            flag = -1
        else:
            if flag == 1:
                break
            left = mid + 1
            flag = 1

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))

    cnt = 0
    for target in b :
        binarySearch(a, target, 0, n-1)
    print(f'#{test_case} {cnt}')