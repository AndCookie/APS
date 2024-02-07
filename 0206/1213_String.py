import sys
sys.stdin = open('1213_input.txt', encoding='utf-8')


# LPS 만들기
def make_LPS(pattern):
    # pattern : 비교대상 문자열
    M = len(pattern)
    LPS = [0] * M

    same_p_idx = 0  # 동일 패턴 인덱스
    idx = 1  # 패턴 체크 인덱스

    while idx < M:
        if pattern[same_p_idx] == pattern[idx]:  # 같은 패턴을 가지고 있으면
            same_p_idx += 1  # 같은 패턴을 발견해서 1증가
            LPS[idx] = same_p_idx  # 일치하는 인덱스가 존재하므로 LPS값 추가
            idx += 1  # 다음 자리를 확인하기 위해 증가
        else:  # 패턴이 다르다면
            if same_p_idx != 0:  # 현재 동일 패턴이 있으면
                same_p_idx = LPS[same_p_idx - 1]  # 패턴을 하나씩 줄이면서 동일 패턴이 있는지 확인
                # 이전의 LPS값으로 동일 패턴 여부 확인
            else:
                LPS[idx] = 0  # 일치하지 않으므로 LPS값은 0
                idx += 1
    # print(LPS)
    return LPS


# KMP 알고리즘
def KMP(P, T):
    M = len(P)  # pattern (찾고자 하는 패턴 문장 short)
    N = len(T)  # target  (패턴이 있는지 확인하려는 문장 long)
    LPS = make_LPS(P)

    p_idx = 0
    t_idx = 0

    while t_idx < N and p_idx < M:
        if P[p_idx] == T[t_idx]:  # 같은 문자인가?
            # 다음 문자를 체크
            p_idx += 1
            t_idx += 1
        else:
            if p_idx != 0:
                p_idx = LPS[p_idx - 1]  # 이전값이 동일한 패턴의 개수
                # 그만큼 비교하지 않고 패턴 찾기 가능
            else:
                t_idx += 1  # 처음부터 틀렸다면

    # 패턴과 일치하는 문자열이 있는지 확인
    ans = 0
    if p_idx == M:  # 찾음
        # 찾은 문자열의 시작 인덱스 반환
        ans += 1

    return ans


for test_case in range(1, 11):
    # LPS + KMP
    tc = input()
    pattern = input()
    target = input()

    result = KMP(pattern, target)
    print(f'#{test_case} {result}')
