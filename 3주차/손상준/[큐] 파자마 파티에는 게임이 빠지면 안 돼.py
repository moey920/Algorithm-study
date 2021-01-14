N, K, M = map(int, input().split())

P = [i for i in range(N)]
M = M - 1

cnt = 1



##해결 못함

while True:
    W = P.index(M)
    WW = (K * cnt) % len(P)) -1
    if W == WW:
        del P[WW]
        print(P)
        break
    else:
        del P[WW]
    cnt += 1
    print(P)
    
print(cnt)
