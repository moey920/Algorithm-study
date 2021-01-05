Num = list(map(int, input().split()))

N = Num[0]
K = Num[1]
X = 1000000009
sum_Z = 0

for i in range(1, N+1):
    Y = i ** K
    Z = Y % X
    sum_Z = sum_Z + Z

Z = sum_Z % X

print(Z)
