#자연수 N입력

N=int(input())

#2^N값 생성

s=2**N

#s를 리스트로 변경

list_s=list(str(s))

#문자열을 정수로 바꾸어서 더한값 출력
sum_s=0
r=[]

for i in list_s :
    r.append(int(i))
print(sum(r))
