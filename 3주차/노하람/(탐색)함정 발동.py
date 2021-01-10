# 함정 2차원 배열 조건에 맞게 초기화, 일단 모든 원소를 '.'으로 초기화
array = [['.']*8 for i in range(8)]

# 8x8 2차원 배열을 돌면서 짝수 배열과 홀수배열에 각각 함정('H')를 넣음
for i in range(8) :
    if i % 2 == 0 :
        for j in range(8) :
            if j % 2 == 0 :
                array[i][j] = 'H'
    else :
        for j in range(8) :
            if j % 2 == 1 :
                array[i][j] = 'H'
# print(array)

# 이 부분이 가장 오래 걸렸는데 그냥 str을 입력받으면서 리스트로 감싸주면 각 문자가 리스트의 원소로 들어옴. 이를 다시 리스트에 append해서 2차원 배열로 만들었음
a= []
for i in range(8) : 
    a.append(list(input()))
# print(a)

# 8x8 배열을 돌면서 입력받은 a[i][j]와 함정이 기록된 array[i][j]에 동시에 H가 있으면 카운트를 올림
count = 0
for i in range(8) :
    for j in range(8) :
        if a[i][j] == 'H' and array[i][j] == 'H' :
            count += 1
        
print(count)
