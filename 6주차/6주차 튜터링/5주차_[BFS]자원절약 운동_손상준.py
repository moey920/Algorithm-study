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
            if pointer[1,2] in link: #와 링크 가능  포인터 위치 확인
                np = link[:] 1 #링크배열 복사
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

