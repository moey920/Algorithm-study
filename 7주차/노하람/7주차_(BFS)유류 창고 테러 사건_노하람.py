"""
풀이 :
1. 처음에 익은 토마토들을 모두 queue에 넣고 탐색을 시작한다.
"""

from collections import deque
from collections import Counter 

N, M = map(int, input().split())
fire = [list(map(int, input().split())) for _ in range(N)] # N행만큼 2차원 리스트로 입력받기
box = [[0]*N for _ in range(N)] # N*N 행렬의 유류 창고 초기화
q = deque()


def bfs() :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 다음위치가 유류창고를 벗어나지 않고 방호벽이 아니라면
            if(0<=nx<N) and (0<=ny<N) and (fire[nx][ny] != 1) : 
            # 질문 : 날짜를 1증가시키면 방호벽 1과 겹치는데 조건을 어떻게 세워야할지
                if fire[nx][ny] == 0 :
                    fire[nx][ny] == fire[x][y] + 1 # 날짜를 하루 더해준다
                    q.append((nx, ny))
                    
                    
# [발화 동시 진행]값이 2인 요소들을 큐에 담기
for i in range(N): 
    for j in range(N): 
        if fire[i][j] == 2: 
            q.append((i, j))
# print(q) # deque([(0, 0), (1, 5), (4, 3), (6, 0), (6, 6)])

bfs()

ans = 0
for i in range(N): 
    for j in range(N): 
        if ans < fire[i][j]: 
            ans = fire[i][j] 
        if fire[i][j] == 0: 
            print(-1)
            exit()
        ans = max(ans, 1) # 1과 배열의 최대값과 비교
print(ans - 1)