import sys
sys.stdin = open('6485_input.txt')

T = int(input())
for test_case in range(1, T+1):
    bus_dict = {}

    for i in range(1, 5001):
        bus_dict[i] = 0

    n = int(input())
    for _ in range(n):
        A,B = map(int, input().split())
        for i in range(A, B+1):
            bus_dict[i] += 1
    # print(bus_dict)

    P = int(input())
    num_list = []
    for _ in range(P):
        k = int(input())
        num_list.append(str(bus_dict[k]))

    print(f'#{test_case} {" ".join(num_list)}')