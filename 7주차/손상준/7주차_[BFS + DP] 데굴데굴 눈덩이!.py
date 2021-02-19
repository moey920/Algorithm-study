# 최대값 계산 
def bfs(x,y):
    dq = deque([[x,y]])
    temp = [[1] * N for _ in range(N)]
    while dq:
        e = dq.popleft()
        for i in range(4):
            new_x = e[0] + dx[i]
            new_y = e[1] + dy[i]

            if (new_x <0 or new_x > N-1 or new_y < 0 or new_y > N-1):
                continue

            elif snow_size[new_x][new_y] > snow_size[e[0]][e[1]] and temp[e[0]][e[1]] >= temp[new_x][new_y] :
                dq.append([new_x, new_y])
                temp[new_x][new_y] = temp[e[0]][e[1]] + 1

    return max(map(max, temp))
                
# 시작가능 지점확인 : 주변보다 가장 작을 때 시작 가능
def is_smallest(x,y):
    smallest = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if (new_x <0 or new_x > N-1 or new_y < 0 or new_y > N-1):
            continue
            
        elif snow_size[new_x][new_y] < snow_size[x][y] :
            smallest = False
            break
            
    return smallest

from sys import stdin
from collections import deque

N = int(input())
snow_size = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(N):
    for j in range(N):
        if is_smallest(i,j) == True:
            ans[i][j] = bfs(i,j)
        
print(max(map(max, ans)))
