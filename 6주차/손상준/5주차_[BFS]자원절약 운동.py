import sys
from collections import deque


def check_links(index, N, M, mapping):
    i = index
    visited = [0] * (N+1)
    links = mapping[:]
    
    dq = deque([[i, 0])
    while dq:
        e = dq.popleft()
        pointer = e[0]
        cnt = e[1] + 1 
        for link in links:
            if pointer in link: #와 링크 가능  포인터 위치 확인
                np = link[:] #링크배열 복사
                np.remove(pointer)
                dq.append([np[0], cnt])
                links.remove(link)
                if visited[np[0]] == 0: #최소 방문 확인
                    visited[np[0]] = cnt
        # print(visited)
    return sum(visited)
    
N, M = map(int, input().split())
mapping = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
min = 999999999
ans_index = 0 

for i in range(1, N+1):
    ans = check_links(i, N, M, mapping)
    if min > ans:
        min = ans
        ans_index = i
        
print(ans_index)


##튜터님 코드

# from collections import deque
 
# def bfs(v):
#     global ans_count
#     area_deque = deque()
#     visited[v] = 1
#     area_deque.append((v, 1))
#     while len(area_deque):
#         temp_v, visit_count = area_deque.popleft()
#         for i in range(1, N+1):
#             if visited[i] == 1 or adj[temp_v][i] == 0:
#                 continue
#             visited[i] = 1
#             ans_count += visit_count
#             area_deque.append((i, visit_count + 1))

# N, M = map(int, input().split())
# relationship = [list(map(int, input().split())) for _ in range(M)]
# adj = [[0]*(N+1) for _ in range(N+1)]
# min_count = 999999999
 
# for i in range(M):
#     adj[relationship[i][0]][relationship[i][1]] = 1
#     adj[relationship[i][1]][relationship[i][0]] = 1

# for i in range(1, N+1):
#     visited = [0] * (N + 1)
#     ans_count = 0
#     bfs(i)
#     if min_count > ans_count:
#         min_count = ans_count
#         result = i

# print(result)