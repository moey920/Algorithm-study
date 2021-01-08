
from itertools import product

N, M = map(int, input().split())

#리스트 컴프리핸션
#list comprehension

ist = [i for i in range(1,N+1)]

for item in product(ist, repeat=M):
    print(*item)