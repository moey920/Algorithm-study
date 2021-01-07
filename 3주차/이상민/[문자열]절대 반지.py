nickname = input()
N = int(input())

rings = [input() for _ in range(N)]

cnt = 0
for ring in rings:
    target = ring + ring
    if nickname in target:
        cnt += 1
print(cnt)