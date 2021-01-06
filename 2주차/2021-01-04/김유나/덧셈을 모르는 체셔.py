N = int(input())

answer = 0

if len(str(N))==2:
    answer = int(str(N)[0]) + int(str(N)[1])
elif len(str(N))==3:
    if int(str(N)[1])==0:
        answer = (9 + int(str(N)[0])) + int(str(N)[2])
    elif int(str(N)[2])==0:
        answer = int(str(N)[0]) + (int(str(N)[1]) + 9)
else:
    answer=20
    
print(answer)
