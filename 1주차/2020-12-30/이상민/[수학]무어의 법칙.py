N = int(input())

target = 2**N
answer = 0

while target > 0:
    answer += target % 10
    target = target // 10

print(int(answer))