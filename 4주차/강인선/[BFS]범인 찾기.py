from collections import deque

def bfs(v):
    count = 0
    q = deque([[v, count]])  #q=[[5, 0]]
    while q:
        v = q.popleft()     #v=[5, 0]                     [15,1]                       [6,1]
        e = v[0]             #e=5                        e=15                          E=6
        count = v[1]        #count=0                     count=1                        COUNT=1
        if not visited[e]:  #visited[5]가 false          visited[15]가 false          [6] false
            visited[e] = True #visited[5]를 true로      visited[15]를 true           [6] ture
            if e == K:          #5!=17                   15 !=17                      6!=17
                return count
            count += 1              #count=0  ->  1           count=2                  2 
            if (e * 3) <= 100000:       #e=5 -> 15               45                   18
                q.append([e * 3, count])  #q=[[15, 1]]      [[6,1][4,1][45,2]]
            if (e + 1) <= 100000:       #e=5 -> 6                  16                   7
                q.append([e + 1, count])  #q=[[15,1][6, 1]]     [[6,1][4,1][45,2][16,2]]
            if (e - 1) >= 1:            #e=5 -> 4                   14                  5
                q.append([e - 1, count])  #q=[[15,1][6,1][4, 1]]    [[6,1][4,1][45,2][16,2][14,2]]
    return count
                
N, K = map(int, input().split())
visited = [False] * 100001
print(bfs(N))