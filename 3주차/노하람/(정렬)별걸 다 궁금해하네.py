# 문제 이해 : n**2개의 모든 쌍의 거리
N = int(input())
X = list(map(int, input().split()))

# 좌표 X를 내림차순으로 정렬 : 모든 좌표쌍의 거리(경우의 수)를 구할 것이기 때문에 좌표의 순서는 중요하지 않음
X.sort(reverse=True)
# print(X)

# 모든 쌍의 거리의 합을 저장하기 위한 a 선언
a= 0
# 좌표값의 최대값부터 최소값까지 반복하면서, 해당 인덱스보다 1만큼 다음 인덱스부터 리스트의 끝까지 X[i]-X[j]의 값을 합한다.
for i in range(N) :
    for j in range(i+1, N) :
        a += int(X[i] - X[j])

# 직선 쌍의 모든 경우의 수라고 했기 때문에 X[j]-X[i]의 경우의 수는 X[i]-X[j]와 같다. 그래서 a*2를 출력한다. 
print(a*2)
    


