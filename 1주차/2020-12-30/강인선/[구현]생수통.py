a=[]
b=[]

for i in range(3):
    a.append(int(input()))

for i in range(2):
    b.append(int(input()))

a.sort()
b.sort()

print(a[0]+b[0]+10)

