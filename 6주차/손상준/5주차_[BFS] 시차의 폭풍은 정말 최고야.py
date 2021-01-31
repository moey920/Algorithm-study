import sys
from collections import deque

l = int(input())

Xs, Ys = map(int, sys.stdin.readline().split())
Xg, Yg = map(int, sys.stdin.readline().split())
visited = [[0]*l for _ in range(l)]

find_x = [-2,-2,1,-1,2,2,1,-1]
find_y = [1,-1,-2,-2,1,-1,2,2]

dq = deque([[Xs,Ys,0]])

def bfs(dq):
    while dq:
        index = dq.popleft()
        x = index[0]
        y = index[1]
        cnt = index[2] +1
        for i in range(8):
            new_x =  x + find_x[i]
            new_y =  y + find_y[i]
            if new_x < 0 or new_y <0 or new_x>=l or new_y >= l:
                continue
            if new_x ==  Xg and new_y == Yg:
                return cnt
            if visited[new_x][new_y] == 0 :
                dq.append([new_x, new_y, cnt])
print(bfs(dq))