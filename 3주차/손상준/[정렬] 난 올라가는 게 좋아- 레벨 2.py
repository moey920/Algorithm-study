## 인덱스 체크를 위한 크기비교

def check_index(value, j, lst):
        if value[1] == lst[j][1]:
            if value[0] > lst[j][0]:
                return False
        elif value[1] > lst[j][1]:
            return False

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

        
lst = [] #재배열하기 위한 리스트

for i in range(N): # 기존 리스트를 순차적으로
    idx = 0
    if i == 0:
        lst.append(W[i])
    else: # 새로 정렬하는 리스트의 값과 비교하여
        for j in range(i): 
            if check_index(W[i], j, lst) == False:
                idx += 1
        lst.insert(idx, W[i]) #새로운 리스트에 추가
        

for item in lst: 
    print(*item)
    
    
    