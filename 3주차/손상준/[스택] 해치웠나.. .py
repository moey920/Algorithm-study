lst = input()
bomb = lst.count('(')
lazer = lst.count(')')

stack = []

if bomb != lazer:
    print("NO")
else:
    for i in range(len(lst)):
        atk = lst[i]
        stack.append(atk)
        bomb = stack.count('(')
        lazer = stack.count(')')
        if bomb < lazer:
            print("NO")
            break
    if  bomb != lazer:
        print("NO")
    else :
        print("YES")