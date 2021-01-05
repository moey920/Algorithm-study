# N값 입력

N=int(input())

# 마음대로 쓸 수 없는 값의 합
sum=0
for i in range(N):
    if (i%3)==0 or (i%5)==0:
        sum+=i
    
        

print(sum)
