import sys
sys.stdin = open('18639_input.txt')

def merge(left, right):
    global cnt
    len_left = len(left)
    len_right = len(right)
    left_i = right_i = i = 0
    result = [0] * (len_left + len_right)

    if left[-1] > right[-1]:
        cnt += 1
    while len_left > left_i or len_right > right_i:
        if len_left > left_i and len_right > right_i:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                left_i += 1
            else:
                result[i] = right[right_i]
                right_i += 1
        elif len_left > left_i:
            result[i] = left[left_i]
            left_i += 1
        elif len_right > right_i:
            result[i] = right[right_i]
            right_i += 1
        i += 1

    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    my_arr = list(map(int, input().split()))
    
    cnt = 0
    new_arr = mergeSort(my_arr)
    
    print(f'#{test_case}', new_arr[n//2], cnt)

