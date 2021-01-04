"""
[구현]주방장 도도새

3줄 요약
길이가 N인 리스트를 순차적으로 탐색.
리스트의 값을 더해가며, 총 주문 처리 시간 > 근무시간이 되면, 주문을 더이상 받지 않는다.
주문 처리가 가능하다면, cnt 값을 늘려가며 처리 개수를 센다.
"""

N, T = map(int, input().split())
orders = input().split()

total = 0
cnt = 0
for order in orders:
    total += int(order)
    if total >= T:
        break
    cnt += 1

print(cnt)