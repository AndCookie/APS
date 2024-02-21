import sys
sys.stdin = open('18524_input.txt')

def pre_order(T):
    global cnt
    if T:
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])


T = int(input())
for test_case in range(1, T+1):
    # E 간선 개수, N 루트 노드
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [0] * (E+2)
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p,c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p
    # print(parent)
    # print(left)
    # print(right)

    cnt = 0
    root = N
    pre_order(root)

    print(f'#{test_case} {cnt}')

