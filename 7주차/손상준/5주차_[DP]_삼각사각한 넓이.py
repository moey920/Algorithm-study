N = int(input())

def t3g4g (N):
    space = [0] * (N+1)
    space[1] = 1 #첫 번째 인자 정의
    
    if N == 1:
        return 1
    else:
        for i in range(1,N):
            space[i+1] = space[i] + 3 * 2**(i-2) #점화식 N까지 계산
    return space[N]

print(t3g4g(N))