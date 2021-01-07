N = input()

answer = ''
for i in range(1, int(N)+1):
    answer += str(i)
    if N in answer:
        break

print(answer.find(N)+1)