import sys
sys.stdin = open('2005_input.txt')


def pascal(n):
    # 처음 1
    if n == 1:
        print(1)
        return [1]
    # 이전 배열
    before = pascal(n-1)
    # 현재 배열
    ans = [1]
    for i in range(n-2):
        ans.append(before[i]+before[i+1])
    ans += [1]
    print(' '.join(map(str, ans)))
    return ans

T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 파스칼 삼각형의 크기

    print(f'#{test_case}')
    result = pascal(N)

