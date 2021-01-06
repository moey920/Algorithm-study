from itertools import product

N, M=map(int, input().split())

list_N=[]


for i in range(N):
    list_N.append(i+1)
    
for i in product(list_N, repeat=M):
    print(*i)


