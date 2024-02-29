import sys
sys.stdin = open('1234_input.txt')

for test_case in range(1, 11):
    N, my_arr = input().split() # 문자의 개수
    stack = []
    my_arrr = list(my_arr)
    stack.append(my_arr[0])

    for i in range(1, int(N)):
        # empty stack이 아니면서
        # stack[-1]과 새로 들어오려는 수가 중복이라면 pop
        if stack and stack[-1] == my_arr[i]:
            stack.pop()
        # stack[-1]과 새로 들어오려는 수가 다르다면 append
        else:
            stack.append(my_arr[i])
    print(f'#{test_case}', end=" ")
    print(*stack, sep="")
