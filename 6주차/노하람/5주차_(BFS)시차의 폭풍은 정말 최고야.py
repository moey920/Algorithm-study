
"""
풀이 :
1. 말의 출발지와 목적지를 받아서 이동가능한 경로를 설정한다.(8가지)
2. deque()에 출발지를 집어넣고 while문을 진행한다.
3. 현재 위치에서 이동가능한 8가지 방향으로 이동하고 해당 좌표들을 1로 바꾼다.(지도를 벗어나지 않는 선에서), 이동하기전에 cnt를 올린다.
4. 만약 이동한 좌표가 목적지의 좌표와 같다면 누적된 cnt를 리턴한다. 아니라면 해당 좌표를 큐에 넣고 다시 해당 자리에서 이동을 시작한다.
"""
# 하람코드
from collections import deque

def bfs():
    global cnt
    cnt = 0
    # 말이 이동 가능한 8가지 경로
    direction = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)] 

    queue = deque() # 탐색을 하려는 좌표를 담는다.
    queue.append((Xs, Ys)) # x,y는 반복증가하는 i,j(세로-가로) 0,0 1,0 2,0 3,0 ... 0,1 1,1 2,1 3,1 ...
    
    while queue: # 빈 큐일 때까지 반복
        now = queue.popleft() # 현재 위치를 pop하여 now에 저장, (0,0)
        cnt += 1

        for i in range(8): # 8가지 이동가능한 가지수를 모두 탐색
            nx = now[0] + direction[i][0] # 현재위치의 x좌표에 이동가능한 리스트의 x value를 더한다.
            ny = now[1] + direction[i][1] # 현재위치의 y좌표에 이동가능한 리스트의 y value를 더한다.
            # print(nx,ny)

            if(0 <= nx < L) and (0 <= ny < L): # 지도를 벗어나지 않는 이동이라면
                if nx == Xg and ny == Yg : # 이동한 곳이 목적지라면
                    return cnt # 이동횟수를 return한다.
                else : # 이동한 곳이 목적지가 아니라면
                    maps[nx][ny] = 1 # 해당 위치를 방문했다고 표시하고
                    queue.append((nx, ny)) # 큐에 다음에 탐색할 값으로 넣는다. (빈 큐가 아니게 되어 while문으로 돌아감)
                    

L = int(input()) # 정사각형 체스판의 한변의 길이인 정수 l을 입력합니다.
Xs, Ys = map(int, input().split()) # 둘째 줄에는 마가 현재 있는 칸(Xs, Ys)
Xg, Yg = map(int, input().split()) # 셋째 줄에는 마의 목적지 칸(Xg, Yg)
maps = [[0]*L for _ in range(L)] # L*L 배열 초기화
bfs()            
print(cnt-1)

"""
정답코드 :
from sys import stdin
from collections import deque
input = stdin.readline

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs():
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(d[x][y])
            return
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not d[nx][ny]:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))


n = int(input())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
d = [[0]*n for _ in range(n)]
bfs()
"""