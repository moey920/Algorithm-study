# [프로그래머스][queue/BFS] 전염병

# 0. 방문 체크 매트릭스 생성 
# 1. 방문 체크 매트릭스에서 백신 맞은 친구들 "V" 로 표기 
# 1.5. 큐 자료 구조 만들고 시작 감염자 추가 - deque
# 2. 반복해서 감염 환자 리스트들을 뽑고 재탐색하도록 - while
# 3. n 시점 시작 환자 수 만큼 반복 : (만약 n 시점 감염자 a,b 라면 a,b에 의해 옮겨진 친구들 한 리스트로 묶기 위해서)
#    n 시점 4방향 탐색하며 시작 환자에 의해 감염된 환자들 확인하고 
#    시작 환자에 의해 감염된 환자들 next_inf_list 리스트로 묶에서 all_inf_deque에 넣기
#    n 시점 시작 환자 수 ,  시작 환자에 의해 감염된 환자들 둘 다 "+" 로 방문 매트릭스 업데이트 
# 4. 시작 환자에 의해 감염된 환자들 수 호가인 
#    --> 있다면 다시 2번으로 돌아가
#    --> 없다면   
#          --> 탐색이 안된 사람이 있는지 확인 (방문 매트릭스 0 포함여부로)  
#         --> 없다면 - 다 탐색하고 감염될 사람 다 감염된거니까 현재시간 반환 

from collections import deque


def solution(m,n,infests,vaccinateds): # n = row, m = col
    visited = [[0 for _ in range(n)] for _ in range(m)]
    moves = ((0, 1), (0, -1), (-1, 0), (1, 0))

    # 1. check vaccinated
    if vaccinateds :
        for one_v in vaccinateds:
            visited[one_v[0]-1][one_v[1]-1] = "V"
    all_inf_deque = deque()
    all_inf_deque.append(infests)


    day = 0
    while all_inf_deque :
        inf_set = all_inf_deque.popleft() # 이번에 탐색할 리스트 뽑기
        next_inf_list = []
        
        for idx in range(len(inf_set)) :
            x, y = inf_set[idx][0], inf_set[idx][1] # 1 index
            if visited[x-1][y-1] == 0 :
                visited[x-1][y-1] = "+" # 시작 점 양성으로 바꾸고

            for dx, dy in moves:
                up_x, up_y = x+dx, y+dy
                if 0 < up_x <= m and 0 < up_y <= n and visited[up_x-1][up_y-1] == 0 and visited[up_x-1][up_y-1]!= 'V':
                    next_inf_list.append((up_x, up_y)) 
                    visited[up_x-1][up_y-1] = "+"


        if len(next_inf_list) != 0:
            all_inf_deque.append(next_inf_list)
            day += 1
        else: # 다음에 탐색할 감염자가 없는 상황
            result = sum(visited, [])
            if 0 in result:
                return -1
            else:
                return day