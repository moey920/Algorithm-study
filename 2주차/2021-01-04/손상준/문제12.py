AB = str(input())

if len(AB) == 3:
    if AB[1] == '0': # if A == 10
        answer = 10 + int(AB[2])
    else: # if B == 10
        answer = 10 + int(AB[0])
    
elif len(AB) < 3: # if A, B < 10
    answer = int(AB[0]) + int(AB[1])
    
else: # if A, B == 10
    answer = 20

print(answer)