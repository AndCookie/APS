import sys
sys.stdin = open('6019_input.txt')

T = int(input())
for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{test_case} {D/(A+B)*F}')