from collections import deque

#상하좌우 이동가능 여부 확인
def is_valid_up(idx1, value):
    if (idx1 - value) >= 0 :
        return True
        
def is_valid_down(idx1, value):
    if   (idx1 + value) < N :
        return True

def is_valid_left(idx2, value):
    if (idx2 - value) >= 0 :
        return True

def is_valid_right(idx2, value):
    if  (idx2 + value) < M :
        return True
        
#이동위치 값 확인
def is_not_zero(idx1, idx2):
    if mapping[idx1][idx2] != '0':
        return True
        
#이동가능할 경우, 이동 
def move(new_location, count):
    count = count +1
    if new_location in dq :
        infinite = True

    elif count > dic[new_location]:
        dic[new_location] = count
        dq.appendleft(new_location)
        
def check_infinite():
    if is_valid_up(idx1, value) == True:
            new_location = (idx1 - value, idx2)
            
            if is_not_zero(new_location[0], new_location[1]):
                move(new_location, count)

    if is_valid_down(idx1, value) == True:
            new_location = (idx1 + value, idx2)

            if is_not_zero(new_location[0], new_location[1]):
                move(new_location, count)

    if is_valid_right(idx2, value) == True:
            new_location = (idx1, idx2 + value)
            
            if is_not_zero(new_location[0], new_location[1]):
                move(new_location, count)

    if is_valid_left(idx2, value) == True:
            new_location = (idx1, idx2 - value)
            
            if is_not_zero(new_location[0], new_location[1]):
                move(new_location, count)
    if infinite == True:
        return True
    
        
        
        

N, M = map(int, input().split())
mapping = list(input() for _ in range(N))

dic = {(i,j) : 0 for i in range(3) for j in range(5)}
dic[(0,0)] = 1

dq = deque([(0,0)])
infinite = False

while dq:

    location = dq.popleft()
    
    idx1 = location[0]
    idx2 = location[1]

    value = int(mapping[idx1][idx2])
    count = dic[location] 
    
    if check_infinite() == True:
        break
    else:  
        check_infinite()
        
if infinite == True:
    print ('-1')
else:
    print(max(list(dic.values())))
