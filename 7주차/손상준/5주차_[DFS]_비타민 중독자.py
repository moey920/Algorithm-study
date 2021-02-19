#DFS로 구현하지 못함.

import sys

M ,N = map(int, sys.stdin.readline().split())
vitamin = [[0] * (M+1) for _ in range(M+1)]

#조합의 수
cnt = 0

#안되는 조합에 대한 입력값을 이차원 배열에 입력 
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    vitamin[x][y] = 1
    vitamin[y][x] = 1
    

# 1~M 까지 중복되지 않도록 탐색
for i in range(1, M+1):
    for j in range(i+1, M+1):
        if vitamin[i][j] == 0: #2가지 조합 확인
            for k in range(j+1, M+1):
                if vitamin[j][k] == 0 and vitamin[i][k] == 0  :
                    cnt += 1 #함께 먹으면 안되는 비타 조합이 아닌 경우 증가
                    
print(cnt)