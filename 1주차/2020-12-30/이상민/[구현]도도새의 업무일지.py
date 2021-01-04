"""
[구현]도도새의 업무일지

B[i] = sigma(A[i]) / i
B[i] * i = sigma(A[i])
A[i+1] = B[i] * (i+1) - sigma(A[i])
"""

N = int(input())

B = list(map(int, input().split()))

A = [B[0]]
for n in range(1, N):
    A.append(B[n] * (n+1) - sum(A))

for i in A:
    print(i, end=" ")