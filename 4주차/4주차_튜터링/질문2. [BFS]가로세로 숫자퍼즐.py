## 질문

# 1. 손으로 직접 다 써가며 푸는 방법 말고 다른 방법의 풀이가 궁금함.
# 2. 해당 유형 문제의 접근법 



## 문제 풀이 코드

##1.

N=int(input())
puzzle=[]
result=[]
mul=1

for i in range(N):
    puzzle.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-3):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num2+=1
        result.append(mul)
        mul=1
for i in range(N-3):
    for j in range(N):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            
        result.append(mul)
        mul=1

for i in range(N-3):
    for j in range(N-3):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            num2+=1
        result.append(mul)
        mul=1
for i in range(N-3):
    for j in range(N-3):
        num1=i
        num2=N-1-j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            num2-=1
        result.append(mul)
        mul=1
print(max(result))


##2.

def main(s) :
    # 가로 방향 탐색
    x = 1
    for i in range(n) :
        for j in range(n-3) :
            x = max(x,s[i][j]*s[i][j+1]*s[i][j+2]*s[i][j+3]) # x에 인덱스 기준으로 첫 최대값부터, 이동가능한 거리까지의 각 최대값을 비교해서 최종 x가 남는다.
    # 세로 방향 탐색
    y = 1
    for i in range(n-3) :
        for j in range(n) :
            y = max(y,s[i][j]*s[i+1][j]*s[i+2][j]*s[i+3][j])
    # 좌상단->우하단 대각선 방향 탐색
    xy = 1
    for i in range(n-3) :
        for j in range(n-3) :
            xy = max(xy,s[i][j]*s[i+1][j+1]*s[i+2][j+2]*s[i+3][j+3])
    # 우상단 -> 좌하단 대각선 방향 탐색
    yx = 1
    for i in range(n-3) :
        for j in range(3,n) :
            yx = max(yx,s[i][j]*s[i+1][j-1]*s[i+2][j-2]*s[i+3][j-3])
            
    print(max(x,y,xy,yx))

if __name__ == "__main__" :
    n = int(input())
    s = [[int(x) for x in input().split()] for y in range(n)]
    main(s)


##3.

from collections import deque
import time

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]


que = deque([0])

for i in range(N): #행을 순차적으로 탐색
    for j in range(N): #열을 순차적으로 탐색
        if (i+3) < N: # 가로 4개
            w = P[i][j] * P[i+1][j] * P[i+2][j] * P[i+3][j]
            if w > max(que): 
                que.append(w)
        if (i+3) < N and (j+3) < N: #우측 대각선 4개
            w = P[i][j] * P[i+1][j+1] * P[i+2][j+2] * P[i+3][j+3]
            if w > max(que): 
                que.append(w)
        if (j+3) < N: #세로 4개
            w = P[i][j] * P[i][j+1] * P[i][j+2] * P[i][j+3]
            if w > max(que): 
                que.append(w)
        if (i+3) < N and (j-3) >= 0: #좌측 대각선 4개
            w4 = P[i][j] * P[i+1][j-1] * P[i+2][j-2] * P[i+3][j-3]
            if w4 > max(que): 
                que.append(w4)
print(max(que))
 
# 시간 측정
#  past = time.ctime()
#  current = time.ctime()
#  gap = current - past