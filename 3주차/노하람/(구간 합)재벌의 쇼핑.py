N = list(map(int, input().split()))

K = list(map(int, input().split()))

# 상품 값을 내림차순으로 정렬
K.sort(reverse=True)

# 최소한으로 구매 가능한 비싼 상품의 개수를 카운트하는 변수
count = 0

# 가장 큰 상품의 값 순서대로 K[i]를 구매가능하면 count를 올리고, N[1] < K[i]라면 그냥 지나간다.
for i in range(len(K)) :
    if N[1] >= K[i] :
        N[1] = N[1] - K[i]
        count += 1
    else :
        continue
# 살 수 있는 상품이 하나도 없었다면 0을 출력한다.
if count == 0 :
    print(0)
else :
    print(count)