nickname=input()

N=int(input())

count_ring=0
count_N=1

while True:
    ring=input()
    
    if nickname in (ring*2):
        count_ring+=1
    count_N+=1
    
    if count_N>N:
        break
        
print(count_ring)