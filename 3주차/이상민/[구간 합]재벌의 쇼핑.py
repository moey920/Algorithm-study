def solution(N, S):
    prices = list(map(int, input().split()))
    cnt_list = []
    for i in range(N):
        for j in range(i+1, N+1):
            price = sum(prices[i:j])

            if price >= S:
                # 구매한 제품의 개수 = j-i
                cnt_list.append(j-i)
                break
    return min(cnt_list) if cnt_list else 0

N, S = map(int, input().split())

print(solution(N, S))