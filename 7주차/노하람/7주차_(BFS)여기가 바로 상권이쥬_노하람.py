"""
풀이 : 
1. BFS를 이용한다
2. 모든 정점을 시작점으로 해서 탐색하되, 해당 좌표가 1이고 상권에 포함(방문체크)
되지 않았다면 다른 상권으로 인식하고 계속 탐색한다
2. 한번 BFS함수를 호출했다면, 해당 시작점에서 연결가능한 모든 1(집)을 탐색하고 같은 상권번호(cnt)를
부여한 후 탐색을 종료한다.
3. 이를 통해 cnt의 개수(상권개수)를 알아낸다.
4. 방문체크(group)을 이용하여 같은 cnt가 부여된 값들을 이용하여 각 상권에 몇 집이나 포함되어 있는지 알아낸다.
"""


from collections import deque
from collections import Counter # 카운터 모듈은 컨테이너 내 동일한 자료가 몇 개 있는지 카운트하며, 결과값을 딕셔너리로 반환해준다.
from functools import reduce

# 입력받기
n = int(input())

# 지도 입력받기 (2차원)
a = [list(map(int,list(input()))) for _ in range(n)]
# print(a)

# 방문 체크용 리스트 (2차원)
group = [[0]*n for _ in range(n)]

# 위 아래 왼 오 방향이동용 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y)) # 현재 탐색하려는 좌표
    group[x][y] = cnt # 현 좌표를 포함해 카운트한 가구의 수로 방문체크를 한다.
    while q:
        x, y = q.popleft()
        
        # 위 아래 왼쪽 오른쪽 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 지도 밖으로 안 나갔는지 확인
            if 0<=nx<n and 0<=ny<n :
                # 집이 있고, 아직 방문한 곳이 아니라면 진행
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny)) # 다음에 탐색할 위치로 nx,ny를 큐에 넣는다.
                    group[nx][ny] = cnt # 해당 위치를 현재 속한 상권번호에 포함시킨다.
    # 여기까지 while문이 돌아가면, 1번상권에 포함된 모든 잡을 찾고 다음엔 2번상권에 포함된 모든 집을 찾고 반복..

# 모든 정점을 시작점으로 해서 탐색
cnt = 0
for i in range(n):
    for j in range(n):
        # 해당 좌표가 상권에 포함되고, 방문체크되지 않았다면
        if a[i][j] == 1 and group[i][j] == 0:
            # 상권번호를 하나 늘리고 bfs를 호출한다.
            cnt += 1
            bfs(i, j, cnt)

# 출력1 : 총 상권의 수를 출력
print(cnt)

# 출력2 : 각 상권내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기 
# ans = reduce(lambda x,y : x+y, group) # reduce는 데이터의 누적을 구할 때 사용한다. sum과 결과는 같음
ans = sum(group, [])
# 상권에 등록된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# cnt(상권번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str,ans))) # join은 특정 문자열을 포함해 리스트를 문자열로 변환해준다.