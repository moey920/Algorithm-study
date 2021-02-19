N, M = map(int, input().split())

def work(N,M):
    lst =[1] * (N+1) #dp를 위한 리스트 생성
    
    if N < M: #예외처리
        return 1
    else:
        for i in range(M,N+1):
            lst[i] = lst[i-1] + lst[i-M]  
            lst[N] %= 1000007
        return lst[N]

print(work(N,M))
    