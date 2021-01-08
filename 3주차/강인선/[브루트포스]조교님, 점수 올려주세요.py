n = int(input())
given = input()

op = [0] * ((n - 1) // 2)

lst = []

def go(idx, flag, hist):
    if idx == (n - 1) // 2:
        lst.append(hist)
        return
    if flag:
        go(idx + 1, False, hist + [0])
    else:
        go(idx + 1, True, hist + [1])
        go(idx + 1, False, hist + [0])

go(0, False, [])

def cal(a, b, oper):
    if oper == "*":
        return a * b
    elif oper == "+":
        return a + b
    elif oper == "-":
        return a - b

ans = -999999999

for case in lst:
    stack = []
    i = 0
    while i < n:
        if i % 2 == 0: # number
            stack.append(given[i])
        else: # oper
            if case[(i - 1) // 2]:
                left = int(stack.pop())
                right = int(given[i + 1])
                stack.append(cal(left, right, given[i]))
                i += 1
            else:
                stack.append(given[i])
        i += 1

    first = int(stack.pop(0))
    for i in range(0, len(stack), 2):
        first = cal(first, int(stack[i + 1]), stack[i])

    ans = max(ans, first)

print(ans)
