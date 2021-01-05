n = int(input())
B = list(map(int, input().split()))

i = 0
A = []
sum_before = 0
sum_now = 0

while i < n:
    #첫 번째 업무일지
    if i == 0:
        A.insert(i, B[i])
        i += 1
    #나머지 업무일지
    else:
        sum_now = B[i]*(i+1)
        sum_before = B[i-1]*i
        A.insert(i, (sum_now - sum_before))
        i += 1

for i in range(n):
    print(str(A[i]), end=' ')
