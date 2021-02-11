from collections import deque
from itertools import combinations

n, m = map(int, input().split())

warehouse=[list(map(int, input().split())) for _ in range(n)]



wherefire=[]


for i in range(n):
    for j in range(n):
        if warehouse[i][j]==2:
            wherefire.append([i,j])
            
canfire=list(combinations(wherefire,m))



dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(lst):
    temp=[]
    time=0
    q=deque()
    for i in lst:
        q.append([i,time])
    while q:
        temp=q.popleft()
        x=temp[0][0]
        y=temp[0][1]
        time=temp[1]
        visited[x][y]=2
        
        
        
        if visited[x][y]==2:
            time+=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<n and 0<=ny<n:
                    
                    if warehouse[nx][ny]==0 and visited[nx][ny]==0:
                        visited[nx][ny]=2
                        q.append([[nx, ny],time])
                    elif warehouse[nx][ny]==1 and visited[nx][ny]==0:
                        visited[nx][ny]=1
                    elif warehouse[nx][ny]==2 and visited[nx][ny]==0:
                        visited[nx][ny]=2
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and warehouse[i][j]==0:
                return(-1)

    return(time-1) 

res=[]

for i in range(len(canfire)):
    visited=[[0]*n for _ in range(n)]
    res.append(bfs(canfire[i]))

if not res:
    print(-1)   
else:
    print(min(res))