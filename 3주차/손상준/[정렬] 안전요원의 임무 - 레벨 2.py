def check_index(value, j, lst):
        if int(value[0]) == int(lst[j][0]): #나이 확인
            if value[1] > lst[j][1]: #알파벳 확인
                return False
        elif int(value[0]) > int(lst[j][0]):
            return False

N = int(input())
W = [list(input().split()) for _ in range(N)]


lst = []

for i in range(N):
    idx = 0
    if i == 0:
        lst.append(W[i])
    else:
        for j in range(i):
            if check_index(W[i], j, lst) == False:
                idx += 1
        lst.insert(idx, W[i])

for item in lst:
    print(*item)
    