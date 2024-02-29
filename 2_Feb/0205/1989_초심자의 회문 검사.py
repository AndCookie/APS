import sys
sys.stdin = open('1989_input.txt')

T = int(input())
for test_case in range(1, T+1):
    my_word = input()

    if my_word == my_word[::-1]:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')
