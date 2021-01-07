from itertools import product

n,m = map(int, input().split())

list_n=list(range(1,n+1))

for i in product(list_n, repeat=m):
    print(*i)
