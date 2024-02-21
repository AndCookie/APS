import sys
sys.stdin = open('1231_input.txt')

def in_order(T):
    if T:
        in_order(left[T])
        print(my_dict[T], end='')
        in_order(right[T])


for test_case in range(1, 11):
    # N 정점 개수
    N = int(input())
    parent = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    my_dict = {}

    for _ in range(N):
        self, char, *kwargs = input().split()
        self = int(self)
        my_dict[self] = char
        try :
            l = int(kwargs[0])
            left[self] = l
            parent[l] = self
            r = int(kwargs[1])
            right[self] = r
            parent[r] = self
        except:
            continue

    # print(parent)
    # print(left)
    # print(right)

    print(f'#{test_case}', end= ' ')
    root = 1
    in_order(root)
    print()

