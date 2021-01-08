N = int(input())
lst_score = [list(map(int, input().split())) for _ in range(N)]

rank = [1] * N
for i in range(N):
    for j in range(N):
        if lst_score[i][0] < lst_score[j][0] and lst_score[i][1] < lst_score[j][1] :
            rank[i] += 1
print(*rank)