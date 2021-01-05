#입력값 생성

a=int(input())

#받은 값을 리스트로 변환

b=list(map(int, list(str(a))))


#합을 구하고 0이 존재하면 10으로 받게 한다
sum=0

for i in b:
    sum+=i
    if i==0:
        sum=sum+9
        
print(sum)
