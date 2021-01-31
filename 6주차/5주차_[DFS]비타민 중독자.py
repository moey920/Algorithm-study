import sys

M ,N = map(int, sys.stdin.readline().split())
vitamin = [[0] * (M+1) for _ in range(M+1)]

cnt = 0

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    vitamin[x][y] = 1
    vitamin[y][x] = 1

for i in range(1, M+1):
    for j in range(i+1, M+1):
        if vitamin[i][j] == 0: #2가지 조합 확인
            for k in range(j+1, M+1):
                if vitamin[j][k] == 0 and vitamin[i][k] == 0: #나머지 조합 확인
                    cnt += 1
                    
print(cnt)