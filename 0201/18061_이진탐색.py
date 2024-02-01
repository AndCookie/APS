import sys
sys.stdin = open('18061_input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # print(P, Pa, Pb)

    def binarySearch(arr, N, key):
        cnt = 0
        start = 0
        end = N-1
        while start <= end:
            middle = (start+end)//2
            if arr[middle] == key:
                cnt += 1
                break
            elif arr[middle] > key:
                end = middle - 1
                cnt += 1
            else:
                start = middle + 1
                cnt += 1
        return cnt

    arr = [i for i in range(1,P+1)]
    cnt_A = binarySearch(arr, P, Pa)
    cnt_B = binarySearch(arr, P, Pb)
    # print(cnt_A, cnt_B)

    result = 0
    if cnt_A > cnt_B:
        result = 'B'
    elif cnt_A < cnt_B:
        result = 'A'

    print(f'#{test_case} {result}')
