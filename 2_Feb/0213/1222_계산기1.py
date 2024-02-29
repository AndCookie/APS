import sys
sys.stdin = open('1222_input.txt')


# for test_case in range(1, 11):
#     N = int(input()) # 문자열 계산식의 길이
#     exp = list(input().split('+'))
#     total = 0
#     for e in exp:
#         total += int(e)
#     print(f'#{test_case} {total}')

for test_case in range(1, 11):
    N = int(input()) # 문자열 계산식의 길이
    exp = list(input())
    stack = [0]
    for e in exp:
        if e.isdecimal():
            stack.append(int(e))
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(x+y)
    print(f'#{test_case} {stack[0]+stack[-1]}')
