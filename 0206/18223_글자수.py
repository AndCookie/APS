import sys
sys.stdin = open('18223_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = set(input())  # 집합
    str2 = input()
    # print(str1)

    my_dict = {}
    maxi = 0
    for s in str1:
        my_dict[s] = 0
        for ss in str2:
            if s == ss:
                my_dict[s] += 1
        if my_dict[s] > maxi:
            maxi = my_dict[s]

    print(f'#{test_case} {maxi}')
