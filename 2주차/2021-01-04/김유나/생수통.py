bottle1 = int(input())
bottle2 = int(input())
bottle3 = int(input())
lid1 = int(input())
lid2 = int(input())

bottle = min(bottle1, bottle2, bottle3)
lid = min(lid1, lid2)

e_water = bottle + lid + 10
print(e_water)