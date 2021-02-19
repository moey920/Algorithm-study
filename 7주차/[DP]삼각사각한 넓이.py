N=int(input())

res=[0 for i in range(N + 1)]
res[0]=1
for i in range(1, N+1):
    res[i]=res[i-1]*2+0.5
print(res[N-1])