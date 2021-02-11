N, A, G, U, D=map(int, input().split())

elevator=[0]*(N+1)


elevator[A]='start'
elevator[G]='finish'

pos=A
cnt=0

while True:
    pos+=U
    if A<=pos<=G:
        
        if elevator[pos]==0:
            elevator[pos]=1
        elif elevator[pos]=='finish':
            print(cnt+1)
            break
    elif N<pos:
        pos-=U
        if elevator[pos-D]==0:
            elevator[pos-D]=1
            pos-=D
        elif elevator[pos-D]==1:
            print('계단을 사용하세요.')
            break
    else:
        print(cnt+1)
        break

    cnt+=1
