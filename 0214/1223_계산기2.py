import sys
sys.stdin = open('1223_input.txt')

for test_case in range(1, 11):
    N = int(input()) # 문자열 계산식의 길이
    exp = list(input())

    # 후위 표기법
    stack = []
    ans = ''
    for e in exp:
        if e.isdecimal():
            ans += e
        elif e == '*':
            while stack and stack[-1] == '*':
                ans += stack.pop()
            stack.append(e)
        elif e == '+':
            while stack:
                ans += stack.pop()
            stack.append(e)
    while stack:
        ans += stack.pop()
    print(ans)

    # 계산
    for a in ans:
        if a.isdecimal():
            stack.append(a)
        elif a == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x)+int(y))
        elif a == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) * int(y))

    print(f'#{test_case} {stack[-1]}')
