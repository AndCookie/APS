import sys
sys.stdin = open('5432_input.txt')

# 10799 쇠막대기
'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''

T = int(input())

for test_case in range(1, T + 1):
    my_arr = input()
    my_arr = my_arr.replace("()", '0')
    stack = []
    ans = 0

    for i in range(len(my_arr)):
        if my_arr[i] == '(':
            stack.append(my_arr[i])
            ans += 1

        elif my_arr[i] == '0':
            ans += len(stack)

        elif my_arr[i] == ')':
            stack.pop()

    print(f'#{test_case} {ans}')