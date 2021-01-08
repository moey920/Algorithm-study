# 중복순열 라이브러리
from itertools import product
N, M = map(int, input().split())

ist = [i for i in range(1, N+1)]

prod = list(product(ist, repeat=M))
for item in prod:
    print(*item)