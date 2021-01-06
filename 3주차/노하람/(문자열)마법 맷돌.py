# 모자장수의 별명을 대문자로 입력
hat = input().upper()
# 도도새가 가지고 있는 반지 개수 입력
n = int(input())
# 모자장수의 반지 개수를 셀 변수 초기화
count = 0

for i in range(n) :
    # 별명이 입력받는 문자열안에 있으면 카운트 증가(반지의 문자열이 끝 글자가 첫 글자로 연결되는 것을 표현하고 싶은데 몰라서 *2했음.)
    if hat in (input().upper()*2) :
        count += 1

print(count)
    
