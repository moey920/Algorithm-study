def countLetters(word):
    
    counter = {}
    for letter in word.lower():
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
        
    return sorted(counter.items(), key = lambda x: x[1], reverse=True)
    
word = input()

counter = countLetters(word)

if len(counter) == 1:
    print(counter[0][0].upper())

elif counter[0][1] == counter[1][1]:
    print("?")
else:
    print(counter[0][0].upper())
