import sys
sys.stdin = open('18528_input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N: 노드 개수, M: 리프노드 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    h = [0] * (N+1)
    for i in range(M):
        leaf, num = map(int, input().split())
        h[leaf] = num

    if N % 2 != 0:  # 홀수라면
        for i in range(N, 1, -2):
            h[i//2]= h[i] + h[i-1]
    else:          # 짝수라면
        h[N//2] = h[N]
        for i in range(N-1, 1, -2):
            h[i//2]= h[i] + h[i-1]

    # print(h)
    print(f'#{test_case} {h[L]}')

