import sys
sys.stdin = open('4408_input.txt')


def f(i, k, s):  # i-1까지 선택한 원소의 합
    global min_v
    if i == k:
        # print(*P)
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return

    else:
        for j in range(i, k):  # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
            f(i + 1, k, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  # 원상복구


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    P = [i for i in range(n)]
    min_v = 100
    f(0, n, 0)
    print(f'#{test_case} {min_v}')
