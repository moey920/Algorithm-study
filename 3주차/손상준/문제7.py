s = str(input())
t = str(input())

def  is_same_word (s, t): #문자열 확인  
    S = len(s)
    V = len(t) // len(s)
    for i in range(S):
        for j in range(V):
            if s[i] == t[i + (S*j)]:
                return(True)
                        
def print_ans(s,t): #정답 출력
    if is_same_word (t,s) == True:
        print(1)
    elif is_same_word (s, t) == True:
        print(1)
    else:
        print(0)

print_ans(s,t)