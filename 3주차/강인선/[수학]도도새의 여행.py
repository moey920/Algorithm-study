R, C, K=map(int, input().split())

visit=[[0 for col in range(R)] for row in range(C)]

if K==1:
    print(1)
    
elif K%2==0:
    if R%2==0 and C%2==0:
        print(1)
    elif R%2==1 and C%2==0:
        print(1)
    else:
        print(0)
else:
    if R%2==0 and C%2==0:
        print(0)
    elif R%2==1 and C%2==0:
        print(0)
    else:
        print(1)
