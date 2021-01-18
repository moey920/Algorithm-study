N = int(input())

for i in range(1,N+1):
    
    if i == 1 or i == 2 : #수열 만들기
        k = [0,1,1]
    else:   # 한개씩 추가
        l = k[i-2] +k[i-1]
        k.append(l)
    
print(k[N])
