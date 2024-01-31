import sys
sys.stdin = open('1945_input.txt')

T = int(input())
for test_case in range(1, T+1):

    my_num = list(input())
    a=b=c=d=e=0

    for i in range(10000000):
        if my_num % 2 == 0 :
        a = my_num//2

    result = 0

    print(f'#{test_case} {result}')