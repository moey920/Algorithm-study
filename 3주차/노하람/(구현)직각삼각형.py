while True :
    V = list(map(int, input().split()))
    M = max(V)
    if M == 0 :
        break
    V.remove(M)
    if V[0]**2 + V[1]**2 == M**2 :
        print('rightangle')
    else :
        print('triangle')