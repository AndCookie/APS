import sys
sys.stdin = open('1859_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N일
    my_arr = list(map(int, input().split())) # N개의 매매가
    
    # 최대값을 맨 오른쪽 값으로 상정
    maxi = my_arr[-1]
    profit = 0
    
    for n in range(N-2, -1, -1):
        # maxi보다 크면 maxi 바꾸기
        if my_arr[n] > maxi:
            maxi = my_arr[n]
        # maxi보다 작으면 차액 더하기
        else:
            profit += maxi - my_arr[n]

    print(f'#{test_case} {profit}')
