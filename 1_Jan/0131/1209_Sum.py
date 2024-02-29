import sys
sys.stdin = open('1209_input.txt')

for test_case in range(1, 11):
    T = int(input())
    my_arr = [list(map(int, input().split())) for _ in range(100)]
    # print(my_arr) # [[3,4,..], [8,9,..], .., [2,7,..]]

    row_total = col_total = diag1_total = diag2_total = 0
    total_list = []

    # 행과 열의 합
    for r in range(100):
        for c in range(100):
            row_total += my_arr[r][c]
            col_total += my_arr[c][r]
        total_list.append(row_total)
        total_list.append(col_total)
        row_total = col_total = 0
    # print(total_list)

    # 대각선의 합
    for idx in range(100):
        diag1_total += my_arr[idx][idx]
        diag2_total += my_arr[99-idx][idx]
    total_list.append(diag1_total)
    total_list.append(diag2_total)
    # print(total_list)

    # 최대값
    maxi = 0
    for t in total_list:
        if maxi <= t:
            maxi = t
    result = maxi
    print(f'#{T} {result}')
