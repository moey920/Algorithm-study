N, M = list(map(int, input().split(' ')))
dp = [0 for i in range(N + 1)]
dp[0] = 1
 
for i in range(1, N+1):
    dp[i] += dp[i - 1]
    if i >= M:
        dp[i] += dp[i - M]
    dp[N] %= 1000007
print(dp[N])