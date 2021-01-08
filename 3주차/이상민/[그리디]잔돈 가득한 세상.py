N = int(input())

moneys = [1000, 100, 10, 1]

charge = 10000 - N

count = 0
for money in moneys:
    count += charge // money
    charge %= money
print(count)