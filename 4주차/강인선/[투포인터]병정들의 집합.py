
N, K=map(int, input().split())

result=[]
soldier=list(map(int, input().split()))

for i in range (N-1):
    for j in range (i+1, N+1):

        if soldier[i:j].count(1)==K:
            result.append(len(soldier[i:j]))
if not result:
    print(-1)
else:
    print(min(result))