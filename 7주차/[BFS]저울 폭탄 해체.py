from collections import deque

a, b, c=map(int, input().split())
visited=[[False]*(b+1) for _ in range(a+1)]
res=[]


def bfs():
    q=deque()
    q.append((0,0))
    visited[0][0]=True
    
    while q:
        x, y = q.popleft()
        z=c-x-y
        if x==0:
            res.append(z)
            
        if x>0 and y<b: #a->b
            w=min(x, b-y)
            if not visited[x-w][y+w]:
                visited[x-w][y+w]=True
                q.append((x-w, y+w))
                
        if x>0 and y<b: #a->b
            w=min(x, b-y)
            if not visited[x-w][y+w]:
                visited[x-w][y+w]=True
                q.append((x-w, y+w))
        if x>0 and z<c: #a->c
            w=min(x, c-z)
            if not visited[x-w][y]:
                visited[x-w][y]=True
                q.append((x-w, y))
                
        if y>0 and x<a: #b->a
            w=min(y, a-x)
            if not visited[x+w][y-w]:
                visited[x+w][y-w]=True
                q.append((x+w, y-w))
                
        if y>0 and z<c: #b->c
            w=min(y, c-z)
            if not visited[x][y-w]:
                visited[x][y-w]=True
                q.append((x, y-w))
                
        if z>0 and x<a: #c->a
            w=min(z, a-x)
            if not visited[x+w][y]:
                visited[x+w][y]=True
                q.append((x+w, y))
                
        if z>0 and y<b: #c->b
            w=min(z, b-y)
            if not visited[x][y+w]:
                visited[x][y+w]=True
                q.append((x, y+w))
                
bfs()
res.sort()
print(' '.join(list(map(str, res))))