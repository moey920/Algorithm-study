N = int(input())
a = []
for i in range(N) :
    a.append([x for x in map(int, input().split())])
# [[55, 85], [58, 83], [88, 86], [60, 75], [46, 55]] 이러한 모양이 나온다. a[0][0] = 55, a[0][1] = 85
b = []
for i in range(N) :
    b.append(N)


for i in range(N) :
    for j in range(2) :
        # j가 0이면 A의 수학점수가 B보다 클 때
        if a[i][j] > a[i+1][j] :
            # A의 과학점수가 B보다 크다면  N등에서 1등 앞서간다.
            if a[i][j+1] > a[i+1][j+1] :
                b[i] -= 1
            else :
                continue
        # A의 수학점수가 B보다 작을 때 N등에서 머무른다.
        elif a[i][j] < a[i+1][j] :
            continue
        # A의 수학점수가 B보다 작을 때 N등에서 머무른다.
        elif a[i][j] == a[i-1][j] :
            continue
print(*b)

# 인덱스때문에 막힘. 반복문을 돌리는데 다음 인덱스의 값과 비교할 때 인덱스 범위를 벗어나는 오류 처리를 어떻게 해야하지?