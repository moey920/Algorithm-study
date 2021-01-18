import time
import sys

sys.setrecursionlimit(10**9)

def add_memoization(n):
    if n in dic:
        return dic[n]
        
    dic[n] = (add_memoization(n-1) + add_memoization(n-2) + add_memoization(n-3)) % 123456
    return dic[n]

N = int(input())
dic = {1:1, 2:2, 3:4}
# start = time.time()
print(add_memoization(N))
# print("time :", time.time() - start)



# import time
# from collections import deque

# start = time.time()
# N = int(input())
# dq = deque([0])
# cnt = 0

# while dq:
#     a = dq.popleft()
    
#     if a == N :
#         cnt = cnt + 1
        
#     if a + 3 <= N :
#         dq.appendleft(a+3)

#     if a + 2 <= N :
#         dq.appendleft(a+2)

#     if a + 1 <= N :
#         dq.appendleft(a+1)

# print(cnt)
# print("time :", time.time() - start)