# n이 증가할 때 마다 각 2차원 좌표의 방문 값을 키, 밸류 값에 저장한다.
n, r, c = map(int, (input().split()))
num = 0
while n > 0 : # n >= 1 이기 때문에 무조건 실행
    a = 2**n // 2 # 2**(n-1)과 같지만 a가 0이 되는 상황을 피하기 위해, a는 이전 n과 다음 n의 구역을 나누는 기준
    if n > 1 :
        if a > r and a <= c :
            num = num + a**2
            c = c - a
        elif a <= r and a > c :
            num = num + (a**2)*2
            r = r - a
        elif a <= r and a <= c :
            num = num + (a**2)*3
            r = r - a
            c = c - a
        # 이 조건에서 걸러지지 않는 a > r and a > c 는 pass되고 아래의 n = n - 1을 실행후 while문을 반복하게 된다.
        # n이 커졌을 때, 이전의 n에서 찾을 수 있는 값을 여기서 찾지 않는 것이다.
        # 예를 들어 n=3, r=7, c=6이 입력되면 num값으로 48을 받고, n=2, r=3, c=2가 되며
        # num값이 12 증가한 60이 되고, n=1, r=1,c=0이 되어 아래의 elif문에서 2를 받아 62가 된다.

    elif n == 1 :
        if r == 0 and c == 1 :
            num = num + 1
        # 대체 왜 (1,0)일때 2를 더하는거지
        elif r == 1  and c == 0 :
            num = num + 2
        elif r == 1 and c == 1 :
            num = num + 3

    n = n - 1

print(num)