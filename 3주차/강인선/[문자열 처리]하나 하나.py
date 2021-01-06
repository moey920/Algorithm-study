from collections import Counter

sentence1 = input()
sentence=sentence1.upper()

counter = Counter(sentence)
check=0



print(counter)
lst_counter_value=list(counter.values())
print(lst_counter_value)


for i in lst_counter_value:
    if i==max(lst_counter_value):
        check+=1
if check<=1:
    print(max(sentence, key=counter.get).upper())
else:
    print('?')