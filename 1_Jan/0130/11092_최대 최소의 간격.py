import sys
sys.stdin = open('11092_input.txt')

T = int(input())
for test_case in range(1, T+1):
    
    cnt = int(input())
    num_list = list(map(int, input().split()))

    maxi=1; mini=10
    for i in range(cnt) :
        if num_list[i] > maxi :
            maxi = num_list[i]
        if num_list[i] < mini :
            mini = num_list[i]

    min_idx = num_list.index(mini)
    num_list.reverse()
    max_idx = cnt - num_list.index(maxi) - 1

    print(f'#{test_case} {abs(max_idx - min_idx)}')
