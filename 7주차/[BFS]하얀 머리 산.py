from collections import deque


N, A, G, U, D=map(int, input().split())

cnt=0
ans=A
dnum=0

if (U-D)!=0 and (G-A)%(U-D)!=0:
    print('계단을 사용하세요.')
elif U!=0 and D!=0 and (U-D)==0 and (G-A)%U!=0:
    print('계단을 사용하세요.')
elif U==0:
    print('계단을 사용하세요.')
else:
    while True:
        ans+=U
        cnt+=1
        if ans==G:
            break
        elif ans>G:
            dnum +=1
            ans=A-(D*dnum)
            cnt=dnum

    print(cnt)
    
    

