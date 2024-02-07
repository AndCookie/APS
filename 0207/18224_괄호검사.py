import sys
sys.stdin = open('18224_input.txt')

T = int(input())
for test_case in range(1, T+1):
    my_arr = input()
    stack = []

    result = 1
    for m in my_arr:
        # 개괄시 append
        if m == '{' or m == '(':
            stack.append(m)
        # 미괄시 pop
        elif m =='}':
            if stack:
                # pop한 것이 짝꿍이 아니라면 append 후 break
                if stack.pop() != '{':
                    stack.append(m)
                    break
            # 빈 stack이면 pop 불가하므로 append 후 break
            else:
                break
        # 미괄시 pop
        elif m == ')':
            if stack:
                # pop한 것이 짝꿍이 아니라면 append 후 break
                if stack.pop() != '(':
                    stack.append(m)
                    break
            # 빈 stack이면 pop 불가하므로 append 후 break
            else:
                break

    # () 짝이 맞지 않아 full stack인 경우
    if stack:
        result = 0
    # () 짝이 맞아 empty stack인 경우
    else:
        result = 1
    print(f'#{test_case} {result}')
