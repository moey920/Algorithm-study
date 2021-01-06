N=int(input())
num=''
for i in range(1, N+1):
    num+=str(i)
    
if str(N) in num:
    print(num.find(str(N))+1)
