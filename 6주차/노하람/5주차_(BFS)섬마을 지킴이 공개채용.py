"""
# 풀이
1. 입력받은 M*N 크기의 2차원 배열을 0으로 초기화하고, K개의 섬 좌표를 입력받아 2차원 배열의 해당 좌표를 1로 변경한다.
2. 땅이 있는 좌표에서 시작해서, 상하좌우로 움직이며 땅이 있는지 검사하고, 있다면 해당 땅을 바다로 바꾸고 해당 좌표로 이동해서 다시 상하좌우를 검사한다.
3. 이렇게해서 이어진 땅을 모두 바다로 바꾸고 해당 지역은 하나의 1로 카운트된다.
"""

from collections import deque

def bfs(x, y):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = deque() #탐색을 하려는 좌표를 담는다.
    queue.append((x, y)) # x,y는 반복증가하는 i,j(세로-가로) 0,0 1,0 2,0 3,0 ... 0,1 1,1 2,1 3,1 ...
    # print(queue) # 0,0부터 살펴보면 queue=[(0,0)]
    
    maps[x][y] = 0 # 해당 지역을 0으로 초기화한다. maps[0][0] = 0
    
    while queue: # 빈 큐일 때까지 반복
        now = queue.popleft() # 현재 위치를 pop하여 now에 저장, (0,0)
        # print(now)

        for i in range(4): #상하좌우 탐색
            nx = now[0] + direction[i][0] # 현재위치의 x좌표에 이동가능한 리스트의 x value를 더한다.
            ny = now[1] + direction[i][1] # 현재위치의 y좌표에 이동가능한 리스트의 y value를 더한다.
            # print(nx, ny)

            if(0 <= nx < N) and (0 <= ny < M): # 지도를 벗어나지 않는 이동이라면
                if maps[nx][ny] == 1: # 현재위치에서 상하좌우로 움직였을 때 땅이 있다면
                    maps[nx][ny] = 0 # 해당 좌표를 바다로 바꾸고
                    queue.append((nx, ny)) # 큐에 다음에 탐색할 값으로 넣는다. (빈 큐가 아니게 되어 while문으로 돌아감)
                    
                    
M, N, K = map(int, input().split()) # 가로 M, 세로 N, 땅의 개수 K
maps = [[0]*M for _ in range(N)] # M*N 배열 초기화
for _ in range(K) :
    i, j = map(int, input().split())
    maps[j][i] = 1 # 입력받은 땅의 좌표를 기록한 maps 획득
cnt = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] != 0 : # 땅에 있다면
            cnt += 1 # 방문처리를 하고
            bfs(i, j) # 이동하는 bfs 함수를 호출한다
            
print(cnt)