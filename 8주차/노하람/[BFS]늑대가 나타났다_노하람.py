"""
풀이 : 
1. 전역변수 양,늑대 / 지역변수 양,늑대를 따로 둔다.
2. 양과 늑대의 위치에서 bfs를 진행한다. 울타리를 만나면 큐에 삽입하지 않는다.(울타리 안, 밖을 따로 돌게 된다.)
3. 해당 구역에서 양인 곳을 sheep_ 변수로 카운트, 늑대인 곳을 wolf_ 변수로 카운트하고 탐색된 지역은 울타리(#)으로 바꿔버린다.
4. 해당 구역에서 양과 늑대의 수를 비교하여 큰 값은 놔두고, 작은 값은 0으로 바꾼다.
5. 울타리 안과 밖에서 각각 살아남은 양과 늑대의 수를 리턴하고, 이를 전역변수에 더해주고 출력한다.

질문 : 5번 테스트케이스 시간초과를 어떻게 해결해야 할지 모르겠습니다.
"""

from collections import deque

def bfs(x, y): 
    sheep_ = 0
    wolf_ = 0

    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((x, y))
    
    while q:
    
        x, y = q.popleft()
        
        if farm[x][y]=='v':
            wolf_ +=1
        if farm[x][y]=='o':
            sheep_ +=1
        farm[x][y]='#'
        
        
        for i in range(4): 
            nx = x + dx[i] 
            ny = y + dy[i] 

            if (0 <= nx < R) and (0 <= ny < C) :
                if farm[nx][ny] != '#' :
                    q.append((nx, ny))
                    
    if sheep_ <= wolf_ :
        sheep_ = 0
    else :
        wolf_ = 0
    return(sheep_, wolf_)




R,C = map(int, input().split())
farm = [list(input()) for _ in range(R)]

# 모든 영역에 대해서 양과 늑대의 숫자를 세기 위한 전역변수
sheep = 0
wolf = 0
    
for i in range(R): # 행 (바깥 리스트) 
    for j in range(C): # 열 (내부 리스트) 
        if farm[i][j]=='v' or farm[i][j]=='o':
            sheep_, wolf_ = bfs(i, j)
            sheep += sheep_
            wolf += wolf_
            
print(sheep, wolf)