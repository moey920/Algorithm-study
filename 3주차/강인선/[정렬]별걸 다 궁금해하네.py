from itertools import combinations

n=int(input())

x=list(map(int, input().split()))

minus_x=[]

com_x=list(combinations(x, 2))

for i in range (len(com_x)):
        minus_x.append(abs(com_x[i][0]-com_x[i][1]))
print(sum(minus_x)*2)
        
