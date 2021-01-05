N = int(input())

list_r = list(str(2**N))

answer = 0
for i in list_r:
    answer = answer + int(i)
    
print(answer)