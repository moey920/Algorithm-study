#데이터의 개수 N

N=int(input())

#데이터 값 입력
data=[]
a=[]
for i in range (N):

    s=int(input())
    data.append(s)

#데이터 값을 리스트로 바꾸어 줌
result=list(map(int, list(str(sum(data)))))

#result를 index0부터 9까지만 추출한 리스트 a생성
for i in range(10):
    a.append(result[i])
    print(a[i], end='')