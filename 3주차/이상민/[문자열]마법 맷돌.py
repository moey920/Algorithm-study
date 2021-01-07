def solution(s, t):
    if s in t:
        if s*2 in t*2:
            return 1
            
    elif t in s:
        if t*2 in s*2:
            return 1
            
    else:
        return 0
    
s = input()
t = input()
print(solution(s, t))