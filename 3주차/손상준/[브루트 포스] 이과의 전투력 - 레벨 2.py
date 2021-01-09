N = int(input())
lst_score = []

#점수 입력받기
for i in range(N):
    score = list(map(int, input().split()))
    lst_score.append(score)

#점수 비교 및 순위 출력

for i in range(N):
    rank = 1
    for j in range (N):
        if lst_score[i][0] < lst_score[j][0] and lst_score[i][1] < lst_score[j][1] :
            rank += 1
    print(rank , end = " ")


## 수정 이전

# #점수 입력받기
# for i in range(N):
#     score = list(map(int, input().split()))
#     lst_score.append(score)

# #점수 비교 및 순위 출력

# for i in range(N):
#     rank = 1
#     for j in range (N):
#         if i != j:
#             if lst_score[i][0] < lst_score[j][0] and lst_score[i][1] < lst_score[j][1] :
#                 rank += 1
#     print(rank , end = " ")
