import sys
sys.stdin = open('18644_input.txt')


def find_set(x):
    # 자기 자신이 대표네 ? 끝
    if parents[x] == x:
        return x
    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return
    # 다른 집합이라면 합침
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(n+1)]

    for idx in range(0, 2*m-1, 2):
        union(arr[idx], arr[idx+1])
    
    group = set()

    for i in range(1, n+1):
        group.add(find_set(i))

    # print(group)
    print(f'#{test_case} {len(group)}')

