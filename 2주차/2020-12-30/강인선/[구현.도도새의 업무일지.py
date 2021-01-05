# 업업무일지 b의 길이를 나타내는 변수 len_b생성

len_b=int(input()) 


# b를 이루는 n개의 정수 입력
a=[]
b=list(map(int, input().split()))
    

for i in range(len_b):
    a.append((b[i])*(i+1)-sum(a))
    print(a[i], end=' ')
