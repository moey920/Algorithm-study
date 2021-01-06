N = input().lower()
# 문자열 처리를 위한 string 라이브러리 import, 소문자를 순서대로 alpa_list에 삽입
import string
alpa_list = []
for i in string.ascii_lowercase: 
       alpa_list.append(i)

#print(alpa_list)
# 입력한 문자열에서 각 알파벳의 수를 카운트한 값을 a 리스트에 삽입
a = []
for i in range(len(alpa_list)) :
    a.append(N.count(alpa_list[i]))
    
#print(a)
# a리스트의 가장 큰 값(많이 나온 알파벳)의 인덱스를 maxi 변수에 넣음
maxi = a.index(max(a))
# a리스트에 가장 큰 값(많이 나온 알파벳)과 중복되는 알파벳이 있는지 찾기 위해 count 변수에 넣음
count = a.count(max(a))

# 가장 많이 나온 알파벳이 여러개가 아니라면, 알파벳 리스트에서 가장 큰 값 인덱스를 찾아 대문자로 출력
if count == 1 :
    print(alpa_list[maxi].upper())
else :
    print('?')

