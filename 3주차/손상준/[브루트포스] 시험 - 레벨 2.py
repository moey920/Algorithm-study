N = int(input())
ANS = input()

blue = ""
red = ""
yellow = ""

# b/r/y 답안지 작성
for i in range(N):
    X = "54321"
    blue = blue + X[i%5]

for i in range(N):
    X = "12345"
    red = red + X[i%5]

for i in range(N):
    X = "33333"
    yellow = yellow + X[i%5]
   
#답안지 기준 채점결과 추철
def score_test (ppl, N, ANS):
    score = 0
    for i in range(N):
        if ppl[i] == ANS[i]:
            score += 1
    return(score)

# 맞은 순서 순위로 리스트에 정렬
R = {
"red" : score_test(red, N, ANS),
"blue": score_test(blue, N, ANS),
"yellow": score_test(yellow, N, ANS),
}

K = []
for i, j in sorted(R.items(), key =lambda x:x[1], reverse = True):
        K.append(j)
        K.append(i)

# 출력
if K[0] == K[2] and K[2] == K[4]:
    print(K[0])
    print(K[1])
    print(K[3])
    print(K[5])

elif K[0] == K[2] :
    print(K[0])
    print(K[1])
    print(K[3])

else:
    print(K[0])
    print(K[1])

