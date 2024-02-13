import sys
sys.stdin = open('18404_input.txt', encoding='utf-8')

def f(i, k):
    if i==k:
        total = 0
        for j in range(k):
            if bit[j]:
                total += nums[j]
        if total == 10:
            return 1
        else:
            return 0
    else:
        # for j in range(2):
        #	bit[i] = j
        #	f(i+1, k)
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)


nums = list(map(int, input().split()))
N = len(nums)
bit = [0]*N   # bit[i] : arr[i]가 부분집합에 포함되었는지 나타내는 배열
ans = 0
ans += f(0, N)       # bit[i]에 1또는0을 채우고, N개의 원소가 결정되면 부분집합을 출력
print(ans)