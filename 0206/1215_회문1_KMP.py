import sys
sys.stdin = open('1215_input.txt')

# Brute-force
for test_case in range(1, 11):
    N = int(input()) # 찾아야하는 회문의 길이
    my_arr = [input() for _ in range(8)]
    # print(my_arr)

    pal_cnt = 0
    # 가로 탐색
    for i in range(0, 8):
        for j in range(0, 8-N+1):
            word = my_arr[i][j:j+N]
            if word == word[::-1]:
                pal_cnt += 1

    # 세로 탐색
    for z in zip(*my_arr):
        # print(list(z))
        for j in range(0, 8-N+1):
            word = z[j:j+N]
            if word == word[::-1]:
                pal_cnt += 1

    print(f'#{test_case} {pal_cnt}')
