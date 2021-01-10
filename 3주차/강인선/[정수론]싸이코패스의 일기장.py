message=input()
code=''

for i in message:
    if ord(i)>=65 and ord(i)<=68:
        s=ord(i) 
        s+=22
        k=chr(s)
        code+=k
    else:
        s=ord(i)
        s-=4
        k=chr(s)
        code+=k

print(code)

