import sys
sys.stdin = open('18222_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    my_arr = [input() for _ in range(N)]
    # print(my_arr)

    result = ''
    # 가로 탐색
    for i in range(0, N):
        for j in range(0, N-M+1):
            word = my_arr[i][j:j+M]
            if word == word[::-1]:
                result = word

    # 세로 탐색
    for z in zip(*my_arr):
        # print(list(z))
        for j in range(0, N-M+1):
            word = z[j:j+M]
            if word == word[::-1]:
                result = "".join(word)

    print(f'#{test_case} {result}')
