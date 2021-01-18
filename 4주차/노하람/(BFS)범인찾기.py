# # 한 단계 진행 시 가능한 경우의 수, 두 단계 진행 시 가능한 경우의 수 ... 이렇게 트리를 넓히면서 탐색하는 알고리즘이 바로 BFS 입니다.
# # (매 단계에서 모든 경우의 수를 탐색)
# # 장점 : 답이 되는 경로가 여러개인 경우에도 최단 경로 보장, 최단 경로가 존재하면 깊이가 무한정 깊어도 답을 찾을 수 있다
# # 단점 : 경로가 길 경우 많은 기억 공간 필요, 해가 존재하지 않는 유한 그래프의 경우 모든 그래프를 탐색 후 실패로 끝난다, 무한 그래프의 경우 해를 찾지도 끝내지도 못한다.

# # 순간이동 (현재위치 * 3)에 우선순위를 두기 위해, 곱하기 인 경우 큐의 좌측에 삽입하여 먼저 처리 될 수 있도록 하였다.

from collections import deque

def bfs(start) :
    
    queue = deque([start]) # 시작 위치와, 인접한 점들을 순차적으로 탐색할 큐를 생성한다
    
    while queue : # 큐가 비어있을 때까지 반복
        now = queue.popleft() # 큐의 가장 왼쪽 원소를 pop()하여 현재 위치(now)로 설정한다.
        
        if now == k : # 현재 위치가 목표 위치에 도달했다면, queue내에 k가 있으면 popleft()를 반복하다보면 now==k가 되어서 리턴된다.
            return visited[now] # 목표위치까지 도달하기 위해 최단거리로 이동한 횟수를 리턴한다.

        # 현재 위치의 인접한 원소로는(그래프로 생각하기) now-1, now+1, now*3이 있고, now*3을 사용가능한 경우 높은 우선순위(가중치)를 가져야 한다.
        for i in (now-1, now+1, now*3) : # i는 다음 위치(now의 인접 원소)
        
            if 0 <= i < max_len and not visited[i] : # 섹터 범위 내로 i(next) 제한, visited[i] 리스트가 비어있지 않으면 
                
                if k >= now*3 == i and i < max_len : # 목표 위치(k)가 now*3(i)보다 같거나 큰 경우 i가 최대 섹션을 넘어가지 않는다면
                    visited[i] = visited[now] + 1 # 다음 인접원소로 이동하기 위한 횟수는 현재 원소로 이동하기 위한 횟수 + 1
                    queue.appendleft(i) # 큐의 좌측에(우선처리 됨) i를 삽입한다
                    # print(queue)
                else : # k가 now*3보다 작다면
                    visited[i] = visited[now] + 1 # 다음 인접원소로 이동하기 위한 횟수는 현재 원소로 이동하기 위한 횟수 + 1
                    queue.append(i) # 1씩 이동하는 인접 원소들을 큐에 삽입한다.(제일 나중에 체크)  


if __name__ == '__main__' :
    max_len = 100000
    n, k = map(int, input().split())
    visited = [0] * max_len # 최단거리로 n이 k로 갈 때 걸리는 횟수(초)를 측정하기 위한 리스트 변수
    print(bfs(n))