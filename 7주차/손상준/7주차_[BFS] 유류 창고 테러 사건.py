#빈 노드 검사하여 bfs()에 전달
def is_valid():
    for i in range(N):
        for j in range(N):
            if checkhouse[i][j] == 0:
                return False

# 시작점 조합 리스트 생성
def find_flamable(N,M):
    flamable = []

    for i in range(N):
        for j in range(N):
            if warehouse[i][j] == 2:
                flamable.append([i,j]) #가연성 index 추출
                
    start = list(combinations(flamable,M)) #중복되지 않는 조합 생성
    return start # main 식으로 전달

# deque를 활용한 bfs 알고리즘을 통해 최소값을 main식에 전달 
def bfs(lst):
    global checkhouse
    global cnt
    checkhouse = copy.deepcopy(warehouse) #이차원배열 전달받은 값으로 초기화 
    cnt = 0
    
    #deque에 전달받은 시작점 append
    dq = deque()
    for i in lst: 
        dq.append([i,0])
    
    #모든 노드 탐색
    while dq:
        dx =  [-1,0,1,0]
        dy =  [0,-1,0,1]
        
        e = dq.popleft()
        x = e[0][0]
        y = e[0][1]
        for i in range(4):
            new_x = x + dx[i] 
            new_y = y + dy[i]
            if new_x >=0 and new_x <= N-1 and new_y >=0 and new_y <=N-1:
                if checkhouse[new_x][new_y] == 0 :
                    checkhouse[new_x][new_y] = 2
                    cnt = e[1] + 1
                    dq.append([[new_x, new_y],cnt])
    
    #탐색완료시 모두 탐색했는지 is_valid()를 통해 검사 
    if is_valid() == False:
        return (-1)
    else:
        return cnt
        

from sys import stdin
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
warehouse = [list(map(int, stdin.readline().split())) for _ in range(N)]
min = 100000000
lst = []

for starts in find_flamable(N,M): #전달받은 시작점들의 리스트를 bfs()에 전달
    lst.append(bfs(starts))

if sum(lst) == (-1)*(len(find_flamable(N,M))): #탐색이 불가능 할 경우
    print(-1)
    
else:  #탐색이 가능할 경우 최소값 출력
    for i in lst:
        if i >= 0:
            if i < min:
                min = i
    print(min)
