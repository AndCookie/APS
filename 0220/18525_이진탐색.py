import sys
sys.stdin = open('18525_input.txt')

def in_order(n):
    global num
    if n <= N:
        # 좌측 노드
        in_order(n * 2)
        # n이 N보다 커지면 n위치에 num(순서) 저장
        arr[n] = num
        # 저장 후, 다음 순서
        num += 1
        # 우측 노드 찾기
        in_order(n * 2 + 1)


T = int(input())
for test_case in range(1, T+1):
    # N 정점 개수, E 간선 개수
    N = int(input())
    arr = [0 for i in range(N + 1)]
    num = 1
    in_order(1)
    # 루트 : 시작 노드
    print(f'#{test_case} {arr[1]} {arr[N // 2]}')


