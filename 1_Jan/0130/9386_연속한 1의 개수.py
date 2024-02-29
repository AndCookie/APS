import sys
sys.stdin = open('9386_input.txt')

T = int(input())
for test_case in range(1, T+1):
    
    length = int(input())
    seq = list(input())

    cnt = 0
    one_cnt = []
    for s in seq:
        if s == '1':
            cnt += 1
        else:
            one_cnt.append(cnt)
            cnt = 0
    one_cnt.append(cnt)

    maxi = 0
    for oc in one_cnt:
        if oc > maxi:
            maxi = oc

    result = maxi
    print(f'#{test_case} {result}')