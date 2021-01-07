A = str(input())
N = int(input())

nickname = []
ans = 0

for i in range(N):
    nickname.append(str(input())*2)

for i in range(N):
    if nickname[i].find(A) == -1:
        ans = ans
    else: 
        ans += 1

print(ans)