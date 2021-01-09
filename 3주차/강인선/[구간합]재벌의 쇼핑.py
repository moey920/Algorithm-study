
N, S=map(int, input().split())

price=list(map(int, input().split()))


sum_price=0

lst=[]

check=1000

for j in range(N):
    for i in price:
        sum_price+=i
        lst.append(i)
        if sum_price==S:
            if len(lst)<check:
                check=len(lst)
            break    
    lst=[]
    sum_price=0
    del price[0]
    
if check!=1000:
    print(check)
else:
    print(0)
