b = list(map(int, input().split()))
w = list(map(int, input().split()))

#청팀/백팀 총점수
B = sum(b)
W = sum(w)

#승리팀 총 점수 출력
if B >= W:
    print(B)
else:
    print(W)
