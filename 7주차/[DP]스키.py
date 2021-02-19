N, M=map(int, input().split())

ski=[list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    ski[i][0] += ski[i - 1][0]
for j in range(1, M):
    ski[0][j] += ski[0][j - 1]

for i in range(1, N):
    for j in range(1, M):
        ski[i][j] += max(ski[i - 1][j], ski[i][j - 1])

print(ski[N - 1][M - 1])