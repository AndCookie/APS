import sys
sys.stdin = open('1860_input.txt')

def start():
    sold_bread = 0
    for person in customers:
        # 공식: 특정 시간에 만들 수 있는 빵의 개수
        made_bread = (person//m) * k

        # 빵을 1개 팔았다
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread
        
        # 재고가 0보다 작으면 실패
        if remain < 0:
            return 'Impossible'
    
    # 실패가 없었으면 성공
    return 'Possible'

T = int(input())
for test_case in range(1, T+1):
    # n 손님수, m초에 k개의 빵 만듦, customers 손님들이 도착하는 시간
    n, m, k = map(int, input().split())
    customers = list(map(int, input().split()))

    customers.sort() # 오름차순 정렬
    result = start()
    print(f'#{test_case} {result}')