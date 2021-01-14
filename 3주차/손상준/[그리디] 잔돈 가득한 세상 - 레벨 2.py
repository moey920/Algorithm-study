M = 10000 -int(input()) #거스름돈
C = [1000, 100, 10, 1] #지폐단위

for i in range(4): #지폐 걔수 리스트 생성
    K = C[i]
    C[i] = M // K
    M = M % K 

print(sum(C)) #지폐 개수 합 출력

## for i in M 
## -> 리스트 요소 모두 출력