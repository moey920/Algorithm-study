#2진수로 인자 받기
N = format(int(input()) + 1, 'b')


#2진수 '4', '7'로 치환
New = N.translate(str.maketrans('01','47'))

#첫자리 제외한 값 출력
print(New[1:])