import sys
sys.stdin = open('5789_input.txt')

T = int(input())

for test_case in range(1, T+1):
    n, q = map(int, input().split())
    box_list = [0 for i in range(n)]
    # print(N, Q, box_list) # 5 2 [0, 0, 0, 0, 0]

    for i in range(1, q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box_list[j] = i

    print(f'#{test_case}', end=" ")
    print(*box_list, sep=" ")