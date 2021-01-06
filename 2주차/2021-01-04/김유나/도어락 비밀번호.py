N1, N2 = map(int, input().split())

rev_N1 = str(N1)[::-1]
rev_N2 = str(N2)[::-1]

answer = int(rev_N1) + int(rev_N2)

print(answer)