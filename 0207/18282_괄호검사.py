import sys
sys.stdin = open('18282_input.txt')

T = int(input())
for test_case in range(1, T+1):
    my_arr = input()
    stack = []
    for m in my_arr:
        # 개괄시 append
        if m == '(':
            stack.append(m)
        # 미괄시 pop
        # 빈 stack이면 pop 불가하므로 append 후 break
        elif m == ')':
            if stack:
                stack.pop()
            else:
                stack.append(m)
                break

    # () 짝이 맞지 않아 full stack인 경우
    if stack:
        result = -1
    # () 짝이 맞아 empty stack인 경우
    else:
        result = 1

    print(f'#{test_case} {result}')
