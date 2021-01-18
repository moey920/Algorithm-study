## 질문

# 1. 문제 실행시, 아래와 같은 오류 발생.

#      RecursionError: maximum recursion depth exceeded in comparison

#      (0/20) 프로그램에서 에러가 발생했습니다. 아래 에러메세지를 읽고 해결해 주세요.
# .elice/runner.sh: line 1:    43 Killed                  python3 -u main.py
# import sys

#   그 이유와 해결 방법을 여쭈어보고 싶음.

# 2. 재귀함수를 이용한 풀이에서 시간초과 문제 해결방법



## 문제 풀이 코드

##1.

##재귀함수를 이용한 풀이-->>>시간 복잡도 N**a --->>>시간초과

# import sys
# sys.setrecursionlimit(10**6)


# def order(N):
#     if N<0:
#         return 0
#     if N==0:
#         return 1
        
#     return order(N-1)+order(N-2)+order(N-3)


# N=int(input())


# print(order(N)%123456)



##점화식을 이용한 계산
N=int(input())
order=[]
order.append(1)
order.append(2)
order.append(4)

for i in range(3, N):
    order.append(order[i-1]+order[i-2]+order[i-3])
    
print(order[-1]%123456)



##2.

import sys # 파이썬은 무한 재귀함수 호출을 제한하기 위해서 1000번 제한이 default이다. 이를 바꿔주기 위한 모듈

def main(n) :
    # n이 1,2,3 일 땐 규칙을 사용할 수 없으므로 예외 처리하는 구문
    if n == 1 : # {1}
        return 1
    if n == 2 : # {1+1, 2}
        return 2
    if n == 3 : # {1+1+1, 1+2, 2+1, 3}
        return 4
    # 재귀함수를 이용
    else :
        return main(n-1)%123456 + main(n-2)%123456 + main(n-3)%123456
        # or
        # return (main(n-1) + main(n-2) + main(n-3))%123456

if __name__ == "__main__" :
    sys.setrecursionlimit(10000) # 재귀함수 호출 제한을 늘려보았지만 시간초과나, 호출 제한(5번 테스트케이스)은 해결하지 못함.
    n = int(input())
    print(main(n))


##3.

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