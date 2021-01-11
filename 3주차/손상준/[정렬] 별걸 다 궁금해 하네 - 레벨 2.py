N = int(input())
lst = list(map(int, input().split()))


# 시간 복잡도 해결 못함
dist_total = [ abs(lst[i] - lst[i+j]) for i in range(N) for j in range(N-i)] 
print(sum(dist_total)*2)


# dist_total = 0

# def check_distance(a, b):
#     c = a - b
#     return(abs(c))
    
# for i in range(N):
#     for j in range(N-i):
#             dist_total = dist_total + check_distance(lst[i],lst[i+j])
# print(dist_total*2)
    