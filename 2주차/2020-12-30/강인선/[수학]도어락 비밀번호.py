#태어난 년도 입력

N1, N2=list(map(str, input().split()))

#변수를 리스트로 변환, 리스트 순서를 역순으로 생성

reverse_N1=int(str(N1)[::-1])
reverse_N2=int(str(N2)[::-1])

#결과값 출력

print(reverse_N1+reverse_N2)