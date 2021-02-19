n, m=map(int, input().split())
dont=[list(map(int, input().split())) for _ in range(m)]
vit=[]

num=1
count=0
while (num<n):

    for i in range(num+1, n):
        vit.append([num, i])
    num+=1
for i in range(m):
    if dont[i] in vit:
        vit.remove(dont[i])

print(len(vit))

