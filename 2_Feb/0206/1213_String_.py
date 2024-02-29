import sys
sys.stdin = open('1213_input.txt', encoding='utf-8')

for test_case in range(1, 11):
    # Brute Force
    tc = input()
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    ans = 0
    for i in range(N - M + 1):
        for j in range(M):
            # 불일치면 다음 시작 위치
            if txt[i + j] != pat[j]:
                break
        # for~else
        # for문이 break 없이 잘 끝났다면
        else:  # 패턴 매칭에 성공하면
            ans += 1

    print(f'#{tc} {ans}')
