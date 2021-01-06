from itertools import combinations

N, M=map(int, input().split())

list_N=[]


for i in range(N):
    list_N.append(i+1)
    
for i in combinations(list_N, M):
    print(*i)
    
    

    


