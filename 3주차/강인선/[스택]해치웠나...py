fight=input()

count1=0
count2=0

index=0
index_m=[]
index_l=[]

index_count=0
check=0

for i in fight:
    if i=='(':
        count1+=1
        index_m.append(index)
    elif i==")":
        count2+=1
        index_l.append(index)
    index+=1

for i in index_l:

    for j in index_m:
        if int(i)<int(j):
            index_count+=1
        if index_count>int(i):
            check=1

    index_count=0
    
    

if count1==count2 and check==0:
    print('YES')
else:
    print('NO')
