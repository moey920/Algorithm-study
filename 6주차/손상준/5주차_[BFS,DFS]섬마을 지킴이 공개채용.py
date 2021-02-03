import sys
sys.setrecursionlimit(10**4)

find_x = [-1,0,1,0]
find_y = [0,1,0,-1]

def dfs(x,y):
    land[x][y] = True
    
    for i in range(4):
        new_x = x + find_x[i]
        new_y = y + find_y[i]
        if new_x < 0 or new_y <0 or new_x>=N or new_y >= M:
            continue
        if sea[new_x][new_y] ==1 and land[new_x][new_y] is False:
            dfs(new_x, new_y)

M, N, K = map(int, sys.stdin.readline().split())
sea = [[0]* M for i in range(N)]
land = [[False]* M for i in range(N)]
cnt = 0

for i in range(K):
    y,x = map(int, sys.stdin.readline().split())
    sea[x][y] = 1

for i in range(N):
    for j in range(M):
        if sea[i][j] ==1 and land[i][j] is False :
            dfs(i, j)
            cnt += 1

print(cnt)
 
