import sys
sys.stdin = open('18400_input.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    # print(arr) # deque([5527, 731, 31274])

    for _ in range(M):
        arr.rotate(-1)

    print(f'#{test_case} {arr[0]}')
