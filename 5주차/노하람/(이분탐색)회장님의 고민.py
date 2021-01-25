N =  int(input()) # 총 사업의 수
biz = list(map(int, input().split())) # 각 사업의 요청예산
M = int(input()) # 총 예산

count = 0 
big_biz = []
mini = M/N # (총 예산/사업 수)보다 작은 요청에 대해서는 수용한다.
for i in range(len(biz)) :
    if biz[i] > mini :
        big_biz.append(biz[i])
        biz[i] = 0

mini_mod = M - sum(biz) # 총 예산 - a = 적은 예산을 빼고 남은 상한액 측정을 위한 예산 

if not len(big_biz) == 0 :
    result = int(mini_mod/len(big_biz))
else :
    result = max(biz)

print(result)