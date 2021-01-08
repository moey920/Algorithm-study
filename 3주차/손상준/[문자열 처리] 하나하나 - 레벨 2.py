from collections import Counter

sentence = str(input()).upper()
counter = Counter(sentence).most_common(2)

# 첫/두 번째 알파벳 사용 횟수 추출
# first_value = counter[0][1]
# second_value = counter[1][1]

# 첫/두 번째 알파벳 추출
# first_key = counter[0][0]
# second_key = counter[1][0]

if len(counter) == 1:
    print(sentence[0])
elif counter[0][1] == counter[1][1] :
    print("?")
else:
    print(counter[0][0])