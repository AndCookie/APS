import sys
sys.stdin = open('18225_input.txt')

T = int(input())
for test_case in range(1, T+1):
    my_arr = list(input())
    stack = []
    # stack 채우고 시작
    stack.append(my_arr[0])

    for i in range(1, len(my_arr)):
        # empty stack이 아니면서
        # stack[-1]과 새로 들어오려는 수가 중복이라면 pop
        if stack and stack[-1] == my_arr[i]:
            stack.pop()
        # stack[-1]과 새로 들어오려는 수가 다르다면 append
        else:
            stack.append(my_arr[i])

    print(f'#{test_case} {len(stack)}')
