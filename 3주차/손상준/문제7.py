s = str(input())
t = str(input())

def is_valid_length (s, t): #문자열 개수가 다른 경우 예외처리
    if len(t) % len(s) == 0: 
        return(True)
        
def  is_same_word (s, t): #문자열 확인  
    S = len(s)
    V = len(t) // len(s)
    for i in range(S):
        for j in range(V):
            if s[i] == t[i + (S*j)]:
                return(True)
                        
def print_ans(s,t): #정답 출력
    if is_valid_length (s, t) != True:
        print(0)
    elif is_same_word (s, t) != True:
        print(0)
    else:
        print(1)

print_ans(s,t)