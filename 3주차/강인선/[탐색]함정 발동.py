
maze=[[0 for col in range(8)] for row in range(8)]
room=[[0 for col in range(8)] for row in range(8)]

count=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            maze[i][j]=1
        else:
            maze[i][j]=0
for i in range(8):
    room[i]=list(input())


for i in range(8):
    for j in range(8):
        if room[i][j]=='H' and maze[i][j]==1:
            count+=1

print(count)
