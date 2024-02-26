import sys
sys.stdin = open('10580_input.txt')

def get_result():
    size = n
    cnt = 0
    for i in range(size):
        for tar in range(i):
            # a 전봇대: 튜플의 첫 번째 요소, b 전봇대: 튜플의 두 번째 요소
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[tar][0], arr[tar][1])
            if i_b < tar_b:
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        # 튜플 형태로 a 전봇대와 b 전봇대를 append
        arr.append((a, b))
    # 첫 번째 원소를 기준으로 오름차순 정렬
    arr.sort(key=lambda x:x[0])
    result = get_result()

    print(f'#{test_case} {result}')

