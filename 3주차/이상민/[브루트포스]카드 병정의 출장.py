from itertools import combinations as cb

N, M = map(int, input().split())

for i in cb([i for i in range(1, N+1)], M):
    print(*i)
