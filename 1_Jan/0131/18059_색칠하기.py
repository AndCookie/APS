import sys
sys.stdin = open('18059_input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    my_arr = [[0]*10 for _ in range(10)]
    # print(my_arr)

    for _ in range(n) :
        r1,c1,r2,c2,color = map(int, input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                my_arr[i][j] += 1
    result = 0
    for ma in my_arr:
        for m in ma:
            # print(m)
            if m == 2 :
                result +=1

    print(f'#{test_case} {result}')
