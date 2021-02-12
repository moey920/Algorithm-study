from collections import deque


def bfs(pos):
    res=[]
    q=deque()
    q.append(pos)
    
    while q:
        x, y, cnt=q.popleft()
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if snowmap[nx][ny]>=snowmap[x][y]:
                    q.append((nx, ny, cnt))

    return (cnt)




n=int(input())
snowmap=[list(map(int, input().split())) for _ in range(n)]

cnt=0
res=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(n):
    for j in range(n):
        res.append(bfs((i,j,cnt)))
        
print(max(res))