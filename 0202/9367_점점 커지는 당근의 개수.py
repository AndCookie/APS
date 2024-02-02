import sys
sys.stdin = open('9367_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    my_arr = list(map(int, input().split()))

    cnt_list =[]
    cnt = 1
    for i in range(1, N):
        if my_arr[i-1] + 1 == my_arr[i]:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1
    cnt_list.append(cnt)

    maxi = 0
    for c in cnt_list:
        if maxi < c:
            maxi = c

    print(f'#{test_case} {maxi}')