#잘못된 설계된 코드 그냥 이차항 배열로 푸는게 좋음

from collections import deque

def get_index(lst, M ,N): #시작점 감염쥐 리스트 만들기
    idx_lst = []
    for i in range(M*N):
        if lst[i] == 1:
            idx_lst.append([i,0])
    return idx_lst

def check_valid(index): # 이동가능 경로 설정
    if (index < (M*N)) == True and (index >= 0) == True:
            if lst[index] == -1:
                return False
            else: 
                return True
    else:
        return False


#입력값 받기
M, N  = map(int, input().split())
mapping = [list(map(int, input().split())) for _ in range(N)]

#map 일차원으로 변환
lst = []
for i in mapping:
    lst = lst + i

#초기값 설정
dq = get_index(lst, M, N)
dq =  deque(dq)
visited = [0 for _ in range(M*N)]
for i in dq:
    visited[i[0]] = 1

while dq:
    e = dq.popleft()
    idx = e[0]
    cnt = e[1]
    if check_valid(idx + 1) == True:
        if (idx + 1) // M == (idx) // M :
            if visited[idx + 1] == 0 :
                visited[idx + 1] = 1
                lst[idx + 1] = 1
                dq.append([idx + 1, cnt + 1])

    if check_valid(idx - 1) == True:
        if (idx - 1 ) // M == (idx) // M :
            if visited[idx - 1] == False :
                visited[idx - 1] = 1
                lst[idx - 1] = 1
                dq.append([idx - 1, cnt + 1])

    if check_valid(idx + M) == True:
        if visited[idx + M] == False :
            visited[idx + M] = 1
            lst[idx + M] = 1
            dq.append([idx + M, cnt + 1])

    if check_valid(idx - M) == True:
        if visited[idx -M] == False :
            visited[idx -M] = 1
            lst[idx -M] = 1
            dq.append([idx - M, cnt + 1])
    ans = cnt

if 0 in lst:
    print(-1)
else:
    print(ans)
