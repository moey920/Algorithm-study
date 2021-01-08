C, S, E = map(int, input().split())

cnt = 0
C = C // 2

while C > 0 and S > 0:
    C -= 1
    S -= 1
    cnt += 1

print(cnt)