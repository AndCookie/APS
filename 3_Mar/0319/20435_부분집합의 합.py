import sys
sys.stdin = open('20435_input.txt')
from itertools import combinations

arr = list(map(int, input().split()))
cnt = 0
for idx in range(len(arr)):
    for c in combinations(arr, idx):
        if sum(c) == 0:
            cnt += 1
print(cnt)

