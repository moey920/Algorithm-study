n = input()

s = 0
for i in n:
    s += int(i)
    if int(i) == 0:
        s += 9
print(s)