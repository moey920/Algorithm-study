from collections import deque


n, m =map(int, input().split())

connect=[list(map(int, input().split())) for _ in range(m)]

lst=list(0 for _ in range(n))

for i in range(m):
    for j in range(2):
        for num in range(1, n+1):
            if connect[i][j]==num:
                lst[num-1]+=1

print(lst.index(max(lst))+1)

