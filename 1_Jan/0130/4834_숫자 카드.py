import sys
sys.stdin = open('4834_input.txt')

T = int(input())
for test_case in range(1, T+1):
    
    cnt = int(input())
    num_list = list(map(int, input()))
    
    # counts 배열 생성
    counts = [0] * 10
    for n in num_list:
        counts[n] += 1

    maxi = 0
    for i in range(10):
        if counts[i] >= maxi :
            maxi = counts[i]
    counts.reverse()
    max_idx = 10 - counts.index(maxi) - 1

    print(f'#{test_case} {max_idx} {maxi}')
