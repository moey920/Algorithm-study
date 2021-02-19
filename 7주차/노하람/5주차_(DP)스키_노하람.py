"""
풀이 :
현재 좌표의 값은 왼쪽이나 위쪽의 최대값에서만 받아올 수 있다는 튜터님 해결방법 이외에 생각나는 것이 없었습니다.
"""

N, M  = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

i,j = 0,0
# dx = (1, 0)
# dy = (0, 1)

for i in range(1, N) :
    field[i][0] += field[i-1][0]

for j in range(1, M) :
    field[0][j] += field[0][j-1]

for i in range(1, N) :
    for j in range(1, M) :
        # 해당 좌표는 위나 왼쪽에서 값을 받기 때문에 위나 왼쪽 중 최대인 값을 더한다.
        field[i][j] += max(field[i-1][j], field[i][j-1])

print(field[i][j])