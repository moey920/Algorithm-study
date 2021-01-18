import fractions

N=int(input())

r=list(map(int, input().split()))

result=[]

for i in r:
    result.append(fractions.Fraction(12, i))

for i in range(1, N):
    
    print(result[i])