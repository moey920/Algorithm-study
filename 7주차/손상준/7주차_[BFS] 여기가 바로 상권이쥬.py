def dfs(x,y):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    global cnt
    cnt += 1 #상권 추가시 상권값 증가
    
    visited[x][y] = True #방문표시
    
    for i in range(4):
        new_x = x + dx[i] 
        new_y = y + dy[i]

        if new_x >= 0 and new_x <= N-1 and new_y >= 0 and new_y <= N-1: #이동가능 확인
            if visited[x + dx[i]][y + dy[i]] == False : #방문 확인
                if district[x+ dx[i]][y + dy[i]] == 1: #상권확인
                    dfs(x + dx[i], y + dy[i]) #다음 상권 확인

    return(cnt) #상권값 check_distirct()로 반환

def check_district():
    global cnt
    district_value = []
    
    for i in range(N):
        for j in range(N):  
            if visited[i][j] == False: #방문 확인
                if district[i][j] == 1: #상꿘 확인
                    district_value.append(dfs(i,j)) #반환된 상권값 상권 리스트에 추가
                    cnt = 0 #상권값 초기화

    district_value = sorted(district_value) #상권값 오름차순 정렬
    
    print(len(district_value)) #상권개수 출력
    
    for value in district_value: #상권값 출력
        print(value)


#입출력 
N = int(input())
district = [list(map(int, str(input()))) for _ in range(N)] 
visited = [[False]*N for _ in range(N)] 
cnt = 0

check_district()
    