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

