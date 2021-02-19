# 1~N까지 함께 먹으면 안되는 종류를 제외하고 3개 선택
"""
풀이 :
1) 가능한 전체 조합의 경우를 구한다
2) 조합되면 안되는 수가 포함된 경우의 수를 구한다
3) 조합할 수 있는 경우의 수 = 전체 조합 - 조합되면 안되는 경우의 수
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)] 안에 [(1, 2), (3, 4), (1, 3)] 로 구성되는 것이 있으면 list.remove()로 없애려고 했는데
# 어떻게 하는건지 잘 모르겠어요.
"""

N, M = map(int, input().split()) # N : 비타민의 종류 수, M : 함께 먹으면 아뇌는 비타민 조합의 개수
no_lists = [list(map(int, input().split())) for _ in range(M)] # 함께 먹으면 안되는 조합 별 각 인덱스
all_lists = []
for i in range(1, N+1) :
    all_lists.append(i)
print(all_lists) # [1, 2, 3, 4, 5]

from itertools import combinations 
all_ = list(combinations(all_lists, 3)) # 조합 가능한 모든 경우의 수
print(all_) # [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
print(no_lists) # [[1, 2], [3, 4], [1, 3]]

# 튜플로 바꾸기
tuple_no_list = []
for i in range(len(no_lists)) :
    tuple_no_list.append(tuple(no_lists[i]))
print(tuple_no_list) # [(1, 2), (3, 4), (1, 3)]

# 검사를 위해 set으로 바꾸기
no_as_set = set(tuple_no_list)
print(no_as_set) # {(1, 2), (1, 3), (3, 4)}
result = any(no_as_set.issuperset(l) for l in all_) 
print(result) # False

# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)] 안에 [(1, 2), (3, 4), (1, 3)] 로 구성되는 것이 있으면 list.remove()로 없애려고 했는데
# 어떻게 하는건지 잘 모르겠어요.

# result = []
# for i in range(len(tuple_no_list)) :
#     for j in range(len(all_)) :
#         if tuple_no_list[i] in all_[j] :
#             result.append(all_[j])
            
# print(result) # [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5)]
# set_ = set(result)
# print(set_)
# for i in range(len(set_)) :
#     if set_ in all_[i]   :
#         (all_.remove(set_[i]))
# print(all_)
