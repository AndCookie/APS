import sys
sys.stdin = open('18544_input.txt')
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder(num):
    if num:
        print(num, end=' ')

        for child in nodes[num]:  # 현재 노드의 모든 자식에 대해
            preorder(child)  # 재귀적으로 전위 순회
            
        # if nodes[num][0] > 0 :  # 첫 번째 자식 노드가 존재하는지 확인
        #     preorder(nodes[num][0])
        # if nodes[num][1] > 1:  # 두 번째 자식 노드가 존재하는지 확인
        #     preorder(nodes[num][1])
    

V = int(input())
nodes = [[] for _ in range(V+1)]
arr = list(map(int, input().split()))
for i in range(0, len(arr), 2):
    parent = arr[i]
    child = arr[i+1]
    nodes[parent].append(child)
# print(nodes) # [[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], [], []]

preorder(1)