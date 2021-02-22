def dfs(x,y):
    visited[x][y] = True
    
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if is_valid(new_x, new_y) == True:
            if [new_x, new_y] in rice and visited[new_x][new_y] == False: 
                dfs(new_x, new_y)
    return None


def is_valid(x, y):
    if x >= 0 and x < M and y >=0 and y < N:
        return True
    else:
        return False


def check_ans():
    ans = 0
    for r in rice:
        if visited[r[0]][r[1]] == False:
            dfs(r[0],r[1])
            ans += 1
    return ans


from sys import stdin, setrecursionlimit

setrecursionlimit(10**4)

M, N, K = map(int, input().split())
rice = [list(map(int, stdin.readline().split())) for _ in range(K)]
visited = [[False] * N for _ in range(M)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

print(check_ans())