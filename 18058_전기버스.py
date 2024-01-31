import sys
sys.stdin = open('18058_input.txt')

T = int(input())
for test_case in range(1, T+1):
    
    K, N, M = map(int, input().split()) # 3, 10, 5
    charge_station = list(map(int, input().split())) # 1 3 5 7 9

    charge = 0
    current = 0

    while current + K < N:  # bus < 10
        for distance in range(K, 0, -1):
            if (current + distance) in charge_station:
                charge += 1
                current += distance
                break
        else:
            charge = 0
            break
    print(f'#{test_case} {charge}')