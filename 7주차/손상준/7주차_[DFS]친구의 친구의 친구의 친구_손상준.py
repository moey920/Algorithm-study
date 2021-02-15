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
                if cnt == 5:
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
        
