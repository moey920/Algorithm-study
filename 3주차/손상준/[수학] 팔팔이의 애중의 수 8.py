L, R = map(int, input().split())

r = R - L
cnt = 0 

l = len(str(r))
M = len(str(L))
K = str(L)[:M-l]

for n in K:
    if n == '8':
        cnt += 1
        
        
print(cnt)