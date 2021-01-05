bottle = [] #물통 가격 리스트
cap = [] #뚜껑 가격 리스트
price_list = [] #가능 가격 리스트

for i in range(3):
    bottle.append(int(input()))

for i in range(2):
    cap.append(int(input()))

for i in range(3):
    for j in range(2):
        price = bottle[i] + cap[j] + 10 #가격
        price_list.append(price)

print(min(price_list)) #최소가격 출력
