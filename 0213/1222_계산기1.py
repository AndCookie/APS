import sys
sys.stdin = open('1222_input.txt')


for test_case in range(1, 11):
    N = int(input()) # 문자열 계산식의 길이
    exp = input()
    stack = []
    for e in exp:
        if e.isdecimal():
            stack.append(e)
        else:
            while len(stack)!=1 :
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)

    print(f'#{test_case} {stack[-1]}')
