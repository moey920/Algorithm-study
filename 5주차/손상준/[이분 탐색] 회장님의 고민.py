## 4번 오답(시간초과 아님)
def fit_budget(index):
    if (M - sum(lst[:i])) % (N-i) == 0:
        ans = (M - sum(lst[:i])) // (N-i)
        return ans

    
N = int(input())
lst = list(map(int, input().split()))
M = int(input())

lst = sorted(lst)
left =[]
ans = 0

if sum(lst) <= M:
    ans = max(lst)
elif (lst[N-2]) < (M - sum(lst[:N-1])) :
    ans = M - sum(lst[:N-1])

else:
    for i in range(N-1):
        if fit_budget(i) == M:
            break
        else:
            left.append((M - sum(lst[:i])) % (N-i))

    idx = left.index(min(left))
    ans = (M - sum(lst[:idx])) // (N-idx)

print(ans)
            
