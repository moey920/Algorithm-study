n = int(input())

moore = str(2 ** n)

length = len(moore) #자리수
sum_moore = 0 #각 자리수 합

for i in range(length):
    sum_moore = sum_moore + int(moore[i])    

print(sum_moore)