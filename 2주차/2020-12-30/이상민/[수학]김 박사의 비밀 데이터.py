N = int(input())

password = str(sum([int(input()) for _ in range(N)]))[:10]

print(password)