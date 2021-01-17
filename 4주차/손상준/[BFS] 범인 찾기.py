from collections import deque

N, K = map(int, input().split())

que = deque([(N,0)])
ans = 1

while que:
    i, cnt = que.popleft()
    if i == K:
        ans = cnt
        break
    if i*3 <= K * 3:
        que.append((i*3, cnt+1))
    if i + 1 <= K :
        que.append((i+1, cnt+1))
    if i - 1 > 0 : 
        que.append((i-1, cnt+1))

print(ans)