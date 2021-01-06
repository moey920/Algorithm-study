s = input()
string = input()
if s in string :
    if s*2 in string*2 :
        print(1)
    else :
        print(0)
elif string in s :
    if string*2 in s*2 :
        print(1)
    else :
        print(0)
else :
    print(0)