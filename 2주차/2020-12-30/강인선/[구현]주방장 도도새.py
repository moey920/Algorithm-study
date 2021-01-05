#들어온 주문의 수 N, 근무시간 T

N, T=map(int, input().split())

#주문을 처리하는데 걸리는 시간

order=list(map(int, input().split()))


sum=0
result=0
for i in order:
    sum=sum+i
    if sum <= T:
        result=result+1
    elif sum > T:
        break
print(result)