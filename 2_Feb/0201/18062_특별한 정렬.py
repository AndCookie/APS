import sys
sys.stdin = open('18062_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr) # [67, 39, 16, 49, 60, 28, 8, 85, 89, 11]

    def selection_sort(arr, N):
        for i in range(N//2):
            max_idx = i
            for j in range(i + 1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        for i in range(N // 2, N):
            min_idx = i
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print(arr) # [89, 85, 67, 60, 49, 8, 11, 16, 28, 39]

        new_arr = []
        asc = arr[:N//2]
        desc = arr[N//2:]

        for i in range(N//2):
            new_arr.append(asc[i])
            new_arr.append(desc[i])

        return new_arr[:10]

    result = selection_sort(arr, N)
    print(f'#{test_case}', end=" ")
    for r in result:
        print(r, end=" ")
    print()