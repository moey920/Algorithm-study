#5번 case 시간초과를 해결하지 못함
# def dfs(node):
#     global cnt 
#     cnt += 1
#     visited[node] = True 

#     if cnt == 5: #여기 위치에서, return 값을 True로 하여 탐색을 종료하려고하는데 왜 안되는지 잘 모르겠습니다 
#         return True  

#     for i in range(N+1): 
#         if visited[i] == False: #탐색된 노드 예외처리
#             if rel[node][i] == 1 or rel[i][node] == 1: #연결관계 노드 탐색
#                 dfs(i)
        
#     visited[node] = False
#     cnt -= 1

from sys import stdin, setrecursionlimit 

setrecursionlimit(1000000000)

#node 깊이 탐색 함수

def dfs(node):
    global cnt #노드 깊이 
    cnt += 1 #새로운 노드 접근시 증가
    visited[node] = True #탐색노드 방문처리
    
    for i in range(N+1): 
        if visited[i] == False: #탐색된 노드 예외처리
            if rel[node][i] == 1 or rel[i][node] == 1: #연결관계 노드 탐색
                dfs(i)
    
    if cnt == 5: #노드 깊이가 5일 경우, True 반환하여 friend()로 전달 (탐색이 cnt > 5 를 넘어 끝까지 재귀가 돌아 해결되지 않을 것으로 생각합니다, for문 위 아래로 조건을 넣어도 해결 안됨)
        return True
    
    #초기화
    visited[node] = False 
    cnt -= 1

def friend(): #0번부터 순차적으로 탐색
    for i in range(N+1):
        if dfs(i) == True:
            return 1
            break
        else:
            return 0
    
    
N, M = map(int, stdin.readline().split())
rel = [[0] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)
cnt = 0

#노드 간선 설정
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    rel[x][y] = 1
    rel[y][x] = 1

#정답 출력
print(friend())
        
