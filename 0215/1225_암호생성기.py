import sys
sys.stdin = open('1225_input.txt')
from collections import deque

for test_case in range(1, 11):
    a = int(input())
    arr = deque(list(map(int, input().split())))
    # print(arr) # deque([9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551])

    while arr[-1] != 0:
        for i in range(1, 6):
            if arr[-1] == 0:
                break
            else:
                arr.rotate(-1)
                if arr[-1] - i < 0:
                    arr[-1] = 0
                else:
                    arr[-1] -= i
    print(f'#{test_case}', end=" ")
    print(*list(arr))
