N = int(input())

n_str = ""

for i in range(1, N+1): #문자열 생성
    n_str = n_str + str(i)

ans = n_str.find(str(N)) + 1 #문자열 인덱스 생성

print(ans)