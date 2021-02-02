
"""
# 풀이
1. 문제의 핵심은 인접행렬이 가장 많은 지역을 찾는 것이다. 예시에서는 3번과 4번이 각각 인접행렬을 3개씩 가지고 있으므로 운송비가 최소인 지역이 된다.
2. 입력된 숫자가 인접행렬을 뜻하므로, 해당 숫자가 몇 번 나오는지 카운트하여, 카운트가 최대인 값을 출력하되 값이 동일하면 최소인 숫자를 출력한다.

# 해설
1. 지역의 수(N)과 교류관계(M) 입력받기
2. 정수를 쪼개여 M번만큼 입력받아 리스트에 저장하기
3. 입력받은 교류관계 리스트를 1차원 리스트로 변환하기
4. 빈 리스트에 1부터 N까지 교류관계에 출현한 지역수를 카운트하여 집어넣기(인접행렬의 개수)
5. 인접행렬이 최대인 인덱스를 찾아 +1하여 출력하기(인덱스가 0부터 시작하기 때문에)
"""

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

# print(a)
one_array = sum(a, [])

answer = []

# print(one_array)
for i in range(1, N+1) :
    answer.append(one_array.count(i))

print(answer.index(max(answer))+1)


"""
# 튜터님 정답 코드
from collections import deque

def bfs(v):
    global ans_count
    area_deque = deque()
    visited[v] = 1
    area_deque.append((v, 1))
    while len(area_deque):
        temp_v, visit_count = area_deque.popleft()
        for i in range(1, N+1):
            if visited[i] == 1 or adj[temp_v][i] == 0:
                continue
            visited[i] = 1
            ans_count += visit_count
            area_deque.append((i, visit_count + 1))
            
N, M = map(int, input().split())
relationship = [list(map(int, input().split())) for _ in range(M)]
adj = [[0]*(N+1) for _ in range(N+1)]
min_count = 999999999

for i in range(M):
    adj[relationship[i][0]][relationship[i][1]] = 1
    adj[relationship[i][1]][relationship[i][0]] = 1

for i in range(1, N+1):
    visited = [0] * (N + 1)
    ans_count = 0
    bfs(i)
    if min_count > ans_count:
        min_count = ans_count
        result = i
        
print(result)
"""