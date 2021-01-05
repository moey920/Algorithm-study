protein = int(input())

cubes = [10, 40, 250]
answer = [0, 0, 0]
i = -1
for cube in cubes[::-1]:
    while protein >= cube:
        protein -= cube
        answer[i] += 1
        # print(cube, answer, protein)
    i -= 1

if protein == 0:
    print(*answer)
else:
    print(-1)
