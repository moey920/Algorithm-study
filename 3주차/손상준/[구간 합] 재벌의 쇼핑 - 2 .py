N, S = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
breaker = False

if S > sum(P) : #최소금액보다 모든 물건 값이 적을 때
    ans = 0
elif S == sum(P) : #최소금액과 모든 물건 값이 같을 때
    ans = N
elif S < min(P) : # 최소금액
    ans = 1
else:
    for i in range(N):
        for j in range(N-i):
            if S < sum(P[j:j+i+1]):
                ans = i
                breaker = True
                break
        if breaker == True :
            break
print(ans)