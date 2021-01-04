N = int(input())

answer = [i for i in range(N) if i % 3 == 0 or i % 5 == 0]

print(sum(answer))