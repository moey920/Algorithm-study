from collections import deque

n=int(input())
info=[[0]*n for _ in range(n)]

for i in range(n):
    m=input()
    for j in range(n):
        info[i][j]=int(m[j])

visited=[[0]*n for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    cnt=0
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    
    while q:
        x, y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if info[nx][ny]==1 and visited[nx][ny]==0:
                    q.append((nx, ny))
                    visited[nx][ny]=1
                    cnt+=1

    return cnt

            
res=[]
res2=[]

for i in range(n):
    for j in range(n):
        res.append(bfs(i,j))
res.sort()

for i in range(n*n):
    if res[i] !=0:
        res2.append(res[i])
print(len(res2))
for i in range(len(res2)):
    print(res2[i])