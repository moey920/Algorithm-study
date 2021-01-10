N=int(input())

point=[list(map(int, input().split())) for _ in range(N)]

point.sort(key= lambda point: (point[1], point[0]))

for i in range(len(point)):
    print(*point[i])
