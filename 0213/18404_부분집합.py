import sys
sys.stdin = open('18404_input.txt', encoding='utf-8')

def f(i, k):
    total = 0
    global cnt
    if i == k:
        for j in range(k):
            if bit[j]:
                total += arr[j]
        if total == 10:
            cnt += 1
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
    return cnt

arr = list(map(int, input().split()))
N = len(arr)
bit = [0]*N    # bit[i] : arr[i]가 부분집합에 포함되었는지 나타내는 배열
cnt = 0
ans = f(0, N) # bit[i]에 1또는0을 채우고, N개의 원소가 결정되면 부분집합을 출력

print(f'#1 {ans}')