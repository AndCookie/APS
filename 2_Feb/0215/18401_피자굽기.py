import sys
sys.stdin = open('18401_input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    # N 화덕크기, M 피자개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizza = deque()
    for i in range(1, M+1):
        pizza.append([i, arr[i-1]])
    # print(pizza) # deque([[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]])
    hwa = deque()

    # 시작상태
    for _ in range(N):
        hwa.append(pizza.popleft())
    # print(hwa)

    # 피자굽기
    while len(hwa) != 1:
        for _ in range(N):
            if len(hwa)==1:
                break
            else:
                if hwa[0][1] == 0: # 치즈가 녹은 경우
                    hwa.popleft()
                    if pizza: # 피자 반죽이 남아있는 경우
                        hwa.appendleft(pizza.popleft())
                else:
                    hwa[0][1] //= 2 # 치즈가 아직 안녹은 경우
                    hwa.rotate(-1)

    print(f'#{test_case} {hwa[0][0]}')
