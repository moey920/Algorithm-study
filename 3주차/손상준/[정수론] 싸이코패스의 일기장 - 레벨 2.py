import string

#암호값 받기
diary = input()

for i in diary:
    if i in 'WXYZ': # WXYZ 경우 암호 해독
        P = string.ascii_uppercase 
        new_idx = P.find(str(i)) - 4
        print(P[new_idx], end = "")
    else: #이외 알파벳 암호 해독
        P = 'WXYZ' + string.ascii_uppercase 
        new_idx = P.find(str(i)) - 4
        print(P[new_idx], end = "")




--

note = input()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''

for i in range(len(note)):
    for j in range(len(alp)):
        if note[i] == alp[j]:
            ans += alp[j-4]
print(ans)