import sys
sys.stdin = open('18060_input.txt')
from itertools import combinations

T = int(input())
for test_case in range(1, T+1):
    arr = [i for i in range(1, 13)]
    n, k = map(int, input().split())
    cnt = 0
    for c in combinations(arr, n):
        if sum(c) == k:
            cnt += 1
    print(f'#{test_case} {cnt}')

