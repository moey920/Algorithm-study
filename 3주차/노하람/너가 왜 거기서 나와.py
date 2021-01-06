# 찾을 정수 N 입력
N = int(input())
# 빈 문자열 a, 연속되는 정수를 저장하기 위한 count 선언
a = ''
count = 0

# 무한루프로 증가되는 정수문자열 생성
while True :
    count += 1
    a += str(count)
    if str(N) in a :
        print(a.find(str(N))+1)
        break
        
# 2번 테스트케이스 시간초과 오답
