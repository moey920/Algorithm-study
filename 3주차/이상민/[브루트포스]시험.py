N = int(input())

result = input()
red = [1, 2, 3, 4, 5] * N
blue = [5, 4, 3, 2, 1] * N
yellow = [3] * N

score = {
    'red': 0,
    'blue': 0,
    'yellow': 0
}
for i in range(N):
    prob = int(result[i])
    if prob == red[i]:
        score['red'] += 1
    if prob == blue[i]:
        score['blue'] += 1
    if prob == yellow[i]:
        score['yellow'] += 1

max_correct = max(score.values())
print(max_correct)
for student in [k for k, v in score.items() if v == max_correct]:
    print(student)