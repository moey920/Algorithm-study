N = int(input())
answer = input()

# 100문제까지 입력받을 수 있으니, 각자의 작성하는 정답 리스트의 개수를 100개까지 생성한다.
red = [1, 2, 3, 4, 5]*20
blue = [5, 4, 3, 2, 1]*20
yellow = [3]*100

# count 변수들을 정수로 초기화
red_count = 0
blue_count = 0
yellow_count = 0

# 각자 문제를 맞춘 개수를 세기 위해 count 변수를 리스트로 생성합니다.
V = [red_count, blue_count, yellow_count]

for i in range(len(answer)) :
    # 정답이 3번인 경우
    if red[i] == blue[i] == yellow[i] == int(answer[i]) :
        V[0] += 1
        V[1] += 1
        V[2] += 1
    # 정답을 각각 맞추었을 경우
    elif red[i] == int(answer[i]) :
        V[0] += 1
    elif blue[i] == int(answer[i]) :
        V[1] += 1
    elif yellow[i] == int(answer[i]) :
        V[2] += 1

# 카운트 리스트의 최대값 인덱스 찾기

print(max(V))
# 정답을 맞춘 개수가 동점일 경우
if V[0] == V[1] == V[2] :
    print('red')
    print('blue')
    print('yellow')
elif V.index(max(V)) == 0 :
    print('red')
elif V.index(max(V)) == 1 :
    print('blue')
elif V.index(max(V)) == 2 :
    print('yello')