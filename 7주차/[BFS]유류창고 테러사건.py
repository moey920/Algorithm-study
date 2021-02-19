from collections import deque
from itertools import combinations


def bfs(lst):
    visited=[[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if warehouse[i][j]==1 or warehouse[i][j]==2:
                visited[i][j]=1
    
    
    q=deque()
    for i in lst:
        visited[i[0]][i[1]]=1
        q.append(i)
    

    while q:
        x, y, time=q.popleft()
        
        time+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if warehouse[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx, ny, time])
                elif warehouse[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                elif warehouse[nx][ny]==2 and visited[nx][ny]==0:
                    visited[nx][ny]=1
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                return (-1)
    
    return (time-1)







n, m = map(int, input().split())

warehouse=[list(map(int, input().split())) for _ in range(n)]

time=0

wherefire=[]


for i in range(n):
    for j in range(n):
        if warehouse[i][j]==2:
            wherefire.append([i,j, time])
            
canfire=list(combinations(wherefire,m))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
res=[]
res2=[]
check=0

for i in canfire:
    res.append(bfs(i))

for i in range(len(canfire)):
    if res[i]!=-1:
        check=1
        res2.append(res[i])

if check==1:
    print(min(res2))
else:
    print(-1)