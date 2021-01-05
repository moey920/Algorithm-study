A = int(input())
B = int(input())
C = int(input())
D = int(input())

total_time = A + B + C + D

m = 0
while total_time >= 60:
    total_time -= 60
    m += 1

s = total_time
print("{}\n{}".format(m, s))