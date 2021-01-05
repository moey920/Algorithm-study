N = list(map(int, input().split()))

p = [0,0]

for i in range(2): # 입력값 배열
    temp_num = int(N[i])
    
    for j in range(4): # 자리수 역순 배열
        rev_num = (temp_num % 10) * (10 ** (3-j))
        temp_num = temp_num // 10
        p[i] = int(p[i]) + rev_num

password = sum(p) #비밀번호 계산
    
print(password)

# 문자열 치환 안됨
# for i in range(2):
#     for j in range(2):
#         n = N[i][j]
#         N[i][j] = N[i][3-j]
#         N[i][3-j] = n
