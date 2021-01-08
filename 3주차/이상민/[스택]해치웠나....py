shield = input()

stack = []

for i in shield:
    stack.append(i)
    if len(stack) >= 2:
        if stack[-2] == '(' and stack[-1] == ')':
            stack = stack[:-2]
if stack:
    print("NO")
else:
    print("YES")