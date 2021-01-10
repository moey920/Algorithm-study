N = input().upper()

# 문자열 처리를 위한 string 라이브러리 import, 대문자를 순서대로 alpa_list에 삽입
import string
alpa_list = []
for i in string.ascii_uppercase: 
       alpa_list.append(i)
# print(alpa_list), 대문자가 순서대로 리스트에 제대로 들어갔는지 확인

# 정답을 받기 위한 code[] 선언
code = []
for i in range(len(N)) : # 입력받은 문자열 길이만큼
    code.append(alpa_list.index(N[i])-4) # 대문자 리스트 중에서 입력받은 해당 문자와 일치하는 인덱스를 찾아 4개 전의 인덱스 값을 code에 저장
    
for i in range(len(N)) :
    print(alpa_list[code[i]], end='') # 알파벳 리스트에서 정답(code)에 해당하는 인덱스의 value를 출력한다.

