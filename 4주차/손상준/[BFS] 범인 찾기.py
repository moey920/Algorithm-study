from collections import deque

N, K = map(int, input().split())

que = deque([(N,0)])
ans = 1
check = [0 for i in range(100001)]

def check_num(a,check):
    if check[a] == 1:
        return False
    else: 
        check[a] = 1
        return True
    
while que:
    i, cnt = que.popleft()
    if i == K:
        ans = cnt
        break
    if i*3 <= 100000:
        if check_num(i*3, check) == True:
            que.append((i*3, cnt+1))
    if i + 1 <= 100000 :
        if check_num(i+1, check)  == True:
            que.append((i+1, cnt+1))
    if i - 1 > 0 : 
        if check_num(i-1, check)  == True:
            que.append((i-1, cnt+1))

print(ans)