n = int(input()) #암호 줄 개수
password_list = [] #암호 리스트

for i in range(n):
    password = int(input())
    password_list.append(password)

password_check = str(sum(password_list)) #암호 합 생성

print(password_check[:10]) #앞에서 10자리수 인 체크 암호 생성
