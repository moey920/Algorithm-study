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