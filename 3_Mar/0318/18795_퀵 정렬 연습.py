import sys
sys.stdin = open('18795_input.txt')

def quickSort(array, start, end) :
    if start >= end:
        return
    
    pivot = start #피벗 초기값 = 첫번째 요소
    left = start+1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
            
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right-=1
            
        if left>right: # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(array, start, right-1)
    quickSort(array, right+1, end)

    return array



T = int(input())
for test_case in range(1, T+1):
    my_arr = list(map(int, input().split()))
    result = quickSort(my_arr, 0, len(my_arr)-1)
    print(f'#{test_case}', *result)
