N, K, M=map(int, input().split())

seat=[i for i in range(1, N+1)]

delete_seat=[]

index_seat=0

for i in range(N):
    index_seat += K-1  
    if index_seat >= len(seat):     
        index_seat = index_seat%len(seat)

    delete_seat.append(seat.pop(index_seat))
    if delete_seat[-1]==M:
        print(delete_seat.index(M)+1)
        break
    


    
