import sys
sys.stdin = open('18544_input.txt')

def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])


# V 정점 개수, E 간선 개수
V = int(input())
E = V-1
arr = list(map(int, input().split()))
left = [0]*(V+1)  # 부모를 인덱스로하여 왼쪽 자식 번호 저장
right = [0]*(V+1)
parent = [0]*(V+1)  # 자식을 인덱스로하여 부모 번호 저장


for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    parent[c] = p

print(parent)
print(left)
print(right)

c = V
while parent[c] != 0:  # 부모가 있으면
    c = parent[c]      # 부모를 새로운 자식으로 두고
root = c            # 더이상 부모가 없으면 root
pre_order(root)


