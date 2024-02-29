import sys
sys.stdin = open('18226_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) // 10
    tape = [0] * (N + 1)
    tape[0] = tape[1] = 1
    for i in range(2, N + 1):
        tape[i] = 2 * tape[i - 2] + tape[i - 1]

    print(f'#{test_case} {tape[N]}')