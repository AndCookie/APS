import sys
sys.stdin = open('18389_input.txt')

operand = '+=*/()'
stack = []

T = int(input())
for test_case in range(1, T + 1):
    exp = input()
    print(f'#{test_case}', end=' ')
    for e in exp:
        if e in operand:
            stack.append(e)
        else:
            print(e, end='')
    while stack:
        print(stack.pop(), end='')


# T = int(input())
# stack = []
# print(f"#{T}", end=' ')
# for i in input():
#     if i.isdecimal():
#         print(i, end='')
#     else:
#         stack.append(i)
# print(''.join(stack[::-1]), end='')