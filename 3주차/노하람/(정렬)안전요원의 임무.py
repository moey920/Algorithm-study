N = int(input())
array = []
for i in range(N) :
    x, y = list(map(str, input().split()))
    array.append((int(x), y))

# 1. lambda 함수에 대해 아직 잘 모르겠음, x를(나이) 키값으로 정렬하는 건 아래와 같다. 리스트에 키, 이름 순으로 받아왔기 때문에.
array.sort(key=lambda x : (x[0],x[1]))

# 2. 인덱스를 쓰는 것 말고 그냥 문자를 기준으로 정렬하는건 어떻게하지??
# array.sort(key=lambda x : x[1])

for x, y in array:
    print(x, y)