# 백준 12968번
R, C, K = map(int, input().split())

# 홀짝 문제이다. 곱해서 짝수가 나오는 경우는 모두 k번 방문할 수 있다.
if (R*C)%2 == 0 :
    print(1)
else : # 단 1행 1열(홀수), 1번 반복하는 경우는 가능한 것으로 친다.
    if R == 1 and C == 1 and K == 1 :
        print(1)
    else :
        print(0)