import sys
sys.stdin = open('1221_input.txt')

T = int(input())
for test_case in range(1, T+1):
    tc, n = input().split()
    my_list = list(input().split())
    # print(my_list)

    str_to_int = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    int_to_str = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
    # print(str_to_int) # 'ZRO': 0
    # print(int_to_str) # 0: 'ZRO'

    new_list= []
    for m in my_list:
        new_list.append(str_to_int[m])

    # 정렬
    for i in range(len(new_list)-1, 0, -1):
        for j in range(0, i):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    # [0,0,0,1,1..9]

    sort_list = []
    for n in new_list:
        sort_list.append(int_to_str[n])

    print(f'#{test_case}')
    print(*sort_list)