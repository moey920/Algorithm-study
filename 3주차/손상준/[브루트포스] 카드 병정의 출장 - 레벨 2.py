
from itertools import combinations
N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]

for item in combinations(lst, M):
    print(*item)