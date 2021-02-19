import sys 

N, M = map(int, input().split())
ski = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#단방향으로 접근시 직접 생성
for i in range(1, N):
    ski[i][0] += ski[i - 1][0]
for j in range(1, M):
    ski[0][j] += ski[0][j - 1]
    

for i in range(1, N): #주변 접근 가능한 곳에서 높은 값을 가져옴
    for j in range(1, M):
        ski[i][j] += max(ski[i - 1][j], ski[i][j - 1])
        
print(ski[N - 1][M - 1])

