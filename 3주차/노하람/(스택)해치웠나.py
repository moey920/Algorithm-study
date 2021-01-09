N = list(input())

# 스택을 리스트로 구현
stack = []
for t in N :
    open_ = '('
    close_ = ')'
    # 현재 들어온 문자열이 open인지 close인지 검사
    if t in open_: # push
        stack.append(t) 
    else: # t in close_ 라면 pop
        # 스택에 요소가 없다면(지울 '('가 없으면) ')'을 push하여 불완전한 스택을 만든다.
        if not stack :
            stack.append(t)
        # 스택에 '('가 쌓여있다면, ')'가 들어올 차례일 때 '('를 pop한다.
        else :
            stack.pop()

# 스택이 빈 리스트라면(괄호가 모두 제거 되었다면) YES 출력
if not stack :
    print("YES")
else :
    print("NO")
