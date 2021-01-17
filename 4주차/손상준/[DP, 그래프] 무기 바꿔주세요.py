# from itertools import permutations

# N = int(input())
# lst = [str(i) for i in range(N)]

# total = list(map(''.join, permutations(lst)))

# cnt = 0

# for i in total:
#     for j in range(N):
#         if i[j] == lst[j] :
#             cnt += 1
#             break
            
# ans = len(total) - cnt
# print(ans)

def get_weapon(n):
    nw= {1:0, 2:1, 3:2}
    if n in nw:
        return nw[n]
    else:
        nw[n] = (n-1) * (get_weapon(n-1) + get_weapon(n-2))
        return nw[n]
        
N = int(input())

print(get_weapon(N))
