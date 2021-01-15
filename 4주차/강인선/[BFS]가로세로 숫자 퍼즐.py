
N=int(input())
puzzle=[]
result=[]
mul=1

for i in range(N):
    puzzle.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-3):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num2+=1
        result.append(mul)
        mul=1
for i in range(N-3):
    for j in range(N):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            
        result.append(mul)
        mul=1

for i in range(N-3):
    for j in range(N-3):
        num1=i
        num2=j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            num2+=1
        result.append(mul)
        mul=1
for i in range(N-3):
    for j in range(N-3):
        num1=i
        num2=N-1-j
        for k in range(4):
            mul*=puzzle[num1][num2]
            num1+=1
            num2-=1
        result.append(mul)
        mul=1
print(max(result))



