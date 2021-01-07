N=int(input())
change=10000-(N-(N//10000)*10000)
lst=[10000, 1000, 100, 10, 1]

count=0



for i in lst:
    count+=change//i
    change-=(change//i)*i
    
print(count)
