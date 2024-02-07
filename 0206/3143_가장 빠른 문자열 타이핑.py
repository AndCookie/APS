import sys
sys.stdin = open('3143_input.txt')

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)

    cnt = -1
    for w in A.split(B):
        cnt += len(w) + 1

    print(f'#{test_case} {cnt}')
