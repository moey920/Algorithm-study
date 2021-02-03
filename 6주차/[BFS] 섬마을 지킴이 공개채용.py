from collections import deque

      
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(pos):
    q=deque()
    q.append(pos)
    
    while len(q) != 0:
        pos=q.popleft()
        
        for i in range(4):
            nx=pos[0]+dx[i]
            ny=pos[1]+dy[i]
            
            if 0<=nx<m and 0<=ny<n:
                if landmap[nx][ny]==1:
                    landmap[nx][ny]=0
                    q.append([nx,ny])

m, n, k = map(int, input().split())



landmap=[[0]*n for _ in range(m)]

for i in range(k):
    x, y = map(int, input().split()) #map 만들기
    landmap[x][y]=1
        
        
count=0

for i in range(n):
    for j in range(m):
        if landmap[j][i]==1:
            count+=1
            bfs([i,j])
print(count)