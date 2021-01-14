R, C, K = map(int, input().split())

if (R*C) % 2 != 0 :
    if K != 1:
        print(0)
    else: 
        print(1)
else:
    print(1)