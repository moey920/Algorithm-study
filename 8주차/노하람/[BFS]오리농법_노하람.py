"""
풀이 : 
1. 현재 위치에서 상하좌우 확인한다.
2. 행렬 범위를 넘지 않고 조건을 만족한다면 지나온 값을 -1로 바꾸고 계속 연결된 지점을 탐색해 나간다.
3. 탐색을 마치면 카운트 값을 1 올려주고, 다른 요소들을 탐색한다.
4. 모든 연결된 부분들을 탐색을 마치면, 부분들이 몇 개인지 출력한다
"""

import sys
sys.setrecursionlimit(10000)

def dfs(x, y): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        
        if (0 <= nx < N) and (0 <= ny < M): 
            if farm[nx][ny] == 1: 
                farm[nx][ny] = -1 
                # print(farm)
                dfs(nx, ny)
                
    


M, N, K = map(int, input().split())
# 방문 체크용 리스트 (2차원)
farm = [[0]*M for _ in range(N)]
cnt = 0

#벼가 있는 공간 표시
for _ in range(K):
    X, Y = map(int,input().split())
    farm[Y][X] = 1
    
for i in range(N): # 행 (바깥 리스트) 
    for j in range(M): # 열 (내부 리스트) 
        if farm[i][j] > 0: 
            dfs(i, j) 
            cnt += 1 # 탐색을 마치면 cnt값을 올려준다
            
print(cnt)
            


