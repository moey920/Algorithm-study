##질문

# 1. 구현 방법을 모름.
# 2. 큐를 이용해 문제를 해결 방법을 모르겠음.

# 3. [큐] 에 대한 기본적인 설명 (개념 및 문제유형)
# 4. 큐를 이용해서 해당 문제를 푸는 접근방법.
#     (제시된 문제를 읽고 코드로 옮기는 상세한 과정 설명)




## 문제 풀이 코드

## 1. 

N, K, M=map(int, input().split())

seat=[i for i in range(1, N+1)]

delete_seat=[]

index_seat=0

for i in range(N):
    index_seat += K-1  
    if index_seat >= len(seat):     
        index_seat = index_seat%len(seat)

    delete_seat.append(seat.pop(index_seat))
    if delete_seat[-1]==M:
        print(delete_seat.index(M)+1)
        break

## 2.

N, K, M = map(int, input().split())

from collections import deque
# queue를 deque 자료 구조로 초기화
queue = deque([])

for i in range(N) :
    queue.append(i+1)

count = 0

while M in queue :
    for i in range(K-1) :
        queue.append(queue[i])
    for i in range(K) :
        queue.popleft()
    count += 1
print(count)

