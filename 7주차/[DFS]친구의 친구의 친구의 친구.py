n, m = map(int, input().split())
friend = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
print(friend)
visited = [False for i in range(n)]

def dfs(v, depth):
    global ans
    visited[v] = True
    if depth == 4:
        ans = True
        return
    for nxt in friend[v]:
        if not visited[nxt]:
            dfs(nxt, depth+1)


ans = False

for i in range(n):
    dfs(i,0)
    visited[i] = False
    if ans:
        break
print(1 if ans else 0)