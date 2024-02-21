import sys
sys.stdin = open('18526_input.txt')

# 최소 힙
def enq(n):
    global last
    last += 1    # 마지막 노드 추가 (완전 이진 트리를 유지하기 위함)
    h[last] = n  # 마지막 노드에 키 값(데이터) 삽입
    # 부모>자식 비교하기
    c = last     # 자식
    p = c//2     # 부모
    # 부모가 존재하면서 부모>자식이면 교환
    while p>=1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * (N + 1)  # 최대힙
    last = 0

    for i in range(N):
        enq(arr[i])

    result = 0
    i = N
    while i >0:
        i //= 2
        result += h[i]

    # print(h)
    print(f'#{test_case} {result}')

