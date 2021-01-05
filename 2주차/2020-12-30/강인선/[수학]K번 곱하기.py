#자연수 N과 K입력

N, K=map(int, input().split())

#K승 값을 저장하는 리스트 생성

list1=[]
result=0
for i in range (N):
    result+=(i+1)**K
#결과값 출력

print(result%1000000009)
