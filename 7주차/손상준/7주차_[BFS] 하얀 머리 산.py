def bfs():
    ans = 0
    
    while dq:
        cur = dq.popleft() #현재위치

        # 이동위치
        up = cur + U
        down = cur - D
        cnt = visited[cur] + 1

        # 정답일 경우 loop 탈출
        if up == G or down == G:
            ans = cnt
            break
        
        # up이 가능할 경우 이동
        if 1 <= up and up <= N:
            if visited[up] == 0:
                visited[up] = cnt
                dq.append(up)
        # down이 가능할 경우 이동
        if 1 <= down and down <= N:
            if visited[down] == 0:
                visited[down] = cnt
                dq.append(down)
    
    #정답 반환
    if ans == 0:
        return '계단을 사용하세요.'
    else:
        return ans


from sys import stdin
from collections import deque

N, A, G, U, D = map(int, stdin.readline().split())
visited = [0] * (N+1)

dq = deque([A])
        
print(bfs())
    