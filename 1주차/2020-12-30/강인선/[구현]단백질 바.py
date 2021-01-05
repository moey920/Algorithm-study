#변수값 설정


peanut=10

chicken=40

pure=250

#단백질 함량 입력

N=int(input())

#단백질 바에 들어가는 큐브개수

s1=N//pure
r1=N%pure
s2=r1//chicken
r2=r1%chicken
s3=r2//peanut
r3=r2%peanut

if r3==0:
    print(s1, s2, s3)
else:
    print(-1)
