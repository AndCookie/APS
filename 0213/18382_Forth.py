import sys
sys.stdin = open('18382_input.txt')

operand = '+-*/'
stack = []

T = int(input())
for test_case in range(1, T + 1):
    exp = list(input().split())
    for e in exp:
        if e.isdecimal():
            stack.append(int(e))
        elif e in operand:
            # stack에 남아있는 피연산자가 2개 이상일 때
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                if e == '+':
                    stack.append(y+x)
                elif e == '-':
                    stack.append(y-x)
                elif e == '*':
                    stack.append(y*x)
                elif e == '/':
                    stack.append(y//x)
                # print(stack)
            # stack에 남아있는 피연산자가 2개 미만이면 연산 불가
            else:
                print(f'#{test_case} error')
                stack.clear()
                break
        elif e == '.':
            # stack에 남아있는 피연산자가 1개면 결과 출력
            if len(stack) == 1:
                print(f'#{test_case} {stack[-1]}')
                stack.clear()
            # stack에 남아있는 피연산자가 1개가 아니라면 에러
            else:
                print(f'#{test_case} error')
                stack.clear()
