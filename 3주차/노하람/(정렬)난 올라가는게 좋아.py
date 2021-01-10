# 2차원 좌표 정렬하기 문제

n = int(input()) # 원소의 개수를 입력받습니다.
array = [] # 배열을 선언합니다.

for i in range(n):
    x, y = map(int, input().split())
    array.append((x, y)) #정수 두 개로 이루어진 배열로 초기화하고, 원소를 하나씩 입력받습니다.

# sorting 같은 경우 보통 key function을 설정해준다. 2차원 좌표 정렬 문제의 경우 y와 x의 자리를 바꿔 
# y값부터 정렬될 수 있도록 작성하였다.
# 예를 들어 제곱수를 크기를 기준으로 soring하고 싶다면 array.sort(key=lambda x : x*x)
array.sort(key=lambda x : (x[1], x[0])) 

for x, y in array:
    print(x, y)