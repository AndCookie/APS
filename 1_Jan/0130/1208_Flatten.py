import sys
sys.stdin = open('1208_input.txt')

for test_case in range(1, 11):
    
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))

    # 버블 정렬
    # 1 1 1 2 3 3 3 4 4 9 10 11 ...
    maxi = 1; mini = 100
    for i in range(mini-1, 0, -1):
        for j in range(0, i):
            if box_list[j] > box_list[j+1]:
                box_list[j], box_list[j+1] = box_list[j+1], box_list[j]
    
    # dump_cnt번 옮겨 평탄화 진행
    while dump_cnt != 0:
        for i in range(100):
            if box_list[i] < box_list[i+1]:
                box_list[i] += 1
                break
        for j in range(99, 1, -1):
            if box_list[j] > box_list[j-1]:
                box_list[j] -= 1
                break
        dump_cnt -= 1

    result = box_list[-1] - box_list[0]
    print(f'#{test_case} {result}')
