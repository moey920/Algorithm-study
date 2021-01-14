from fractions import Fraction 
#분수형태로 계산하는 모듈
N = int(input())
H = list(map(int, input().split()))

for i in range (1,N):
    ans = Fraction(H[0], H[i])

    if  "/" not in str(ans): #분모가 1일 경우 변환 출력
        print (str(ans) + "/1")
    else:

        print (ans)
