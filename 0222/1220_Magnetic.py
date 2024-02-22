import sys
sys.stdin = open('18529_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, hex = input().split()
    dec = int(hex, base=16) # 16진수 -> 10진수
    b = format(dec, 'b')    # 10진수 -> 2진수
    print(f'#{test_case} {b.zfill(4*int(N))}') # 자릿수 맞춰 0채우기