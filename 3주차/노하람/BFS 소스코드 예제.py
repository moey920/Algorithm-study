# 한 단계 진행 시 가능한 경우의 수, 두 단계 진행 시 가능한 경우의 수 ... 이렇게 트리를 넓히면서 탐색하는 알고리즘이 바로 BFS 입니다.
# (매 단계에서 모든 경우의 수를 탐색)
# 장점 : 답이 되는 경로가 여러개인 경우에도 최단 경로 보장, 최단 경로가 존재하면 깊이가 무한정 깊어도 답을 찾을 수 있다
# 단점 : 경로가 길 경우 많은 기억 공간 필요, 해가 존재하지 않는 유한 그래프의 경우 모든 그래프를 탐색 후 실패로 끝난다, 무한 그래프의 경우 해를 찾지도 끝내지도 못한다.


from collections import deque

# BFS 메서드 정의 (BFS : Breath First Search)
def bfs(graph, start, visited) :
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v] : # v는 현재 방문한 원소, 원소의 방문하지 않은 인접한 원소를 찾는 것
            if not visited[i] : # 방문하지 않았다면
                queue.append(i) # i를 큐에 더한다
                visited[i] = True # i를 방문처리한다.

# 각 노드가 연결된 정보를 표현 (그래프 -> 2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 # 모두 False로 초기화

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)