N = int(input())
sum_patent = 0 #특허가 걸려 마음대로 쓸 수 없는 수들의 합

for i in range(N):
    if i % 3 == 0: #3의 배수 합
        sum_patent = sum_patent + i
    elif i % 5 == 0: # 5의 배수 합 (3의 배수를 제외한)
        sum_patent = sum_patent + i

print(sum_patent)
