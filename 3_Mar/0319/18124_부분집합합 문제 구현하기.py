import sys
sys.stdin = open('18124_input.txt')
from itertools import combinations

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, len(arr)):
        for c in combinations(arr, i):
            if sum(c) == 0:
                result = 1
                break
    print(f'#{test_case} {result}')

