from collections import deque

def get_index(lst, M ,N):
    idx_lst = []
    for i in range(M*N):
        if lst[i] == 1:
            idx_lst.append([i,0])
    return idx_lst

def check_visit(index, visited):
    if visited[index] == 1 :
        return True

def check_valid(index , M, N):
    if index <= (M*N) and index < 0 :
        return True


#입력값 받기
M, N  = map(int, input().split())
mapping = [list(map(int, input().split())) for _ in range(N)]

#map 일차원으로 변환
lst = []
for i in mapping:
    lst = lst + i

dq = get_index(lst, M, N)
dq =  deque(dq)
visited = [0 for _ in range(M*N)]

while dq :
    e = dq.popleft()
    idx = e[0]
    cnt = e[1]
    if check_visit(idx, visited) == False :
        visited[idx] == 1
        if check_valid(idx + 1, M, N) == True and check_visit(idx + 1, visited) == False:
            dq.append([idx + 1, cnt + 1])
        if check_valid(idx - 1, M, N) == True and check_visit(idx - 1, visited) == False:
            dq.append([idx - 1, cnt + 1])
        if check_valid(idx + M, M, N) == True and check_visit(idx + M, visited) == False:
            dq.append([idx + M, cnt + 1])
        if check_valid(idx - M, M, N) == True and check_visit(idx - M, visited) == False:
            dq.append([idx - M, cnt + 1])
    ans = cnt

print(ans)
