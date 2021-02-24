def is_valid(x,y):
    if x >=0 and x < R and y >=0 and y < C:
        return True
    else: 
        return False


def is_wall(x,y):
    if field[x][y] == '#':
        return True
    else:
        return False


def bfs(x,y):
    visited[x][y] = True
    dq= deque([[x,y]])
    counter = [0,0]
    
    while dq:
        e = dq.popleft()

        if field[e[0]][e[1]] == 'o':
            counter[0] = counter[0] + 1
            
        if field[e[0]][e[1]] == 'v':
            counter[1] = counter[1] + 1
            
        for i in range(4):
            new_x = e[0] + dx[i]
            new_y = e[1] + dy[i]
            
            if is_valid(new_x, new_y) == True:
                if visited[new_x][new_y] == False:
                    if is_wall(new_x, new_y) == False:
                        dq.append([new_x, new_y])
                        visited[new_x][new_y] = True

    return counter
    
def check_sheep_win(lst):
    if lst[0] > lst[1]:
        return True
    else: 
        return False

from collections import deque

R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

ans = [0,0]

for i in range(R):
    for j in range(C):
        if visited[i][j] == False and is_wall(i,j) == False:
            lst = bfs(i,j)
            if check_sheep_win(lst) == True:
                ans[0] = ans[0] + lst[0]
            else:
                ans[1] = ans[1] + lst[1]

print(ans[0], ans[1])