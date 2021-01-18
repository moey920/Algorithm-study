def main(s) :
    # 가로 방향 탐색
    x = 1
    for i in range(n) :
        for j in range(n-3) :
            x = max(x,s[i][j]*s[i][j+1]*s[i][j+2]*s[i][j+3]) # x에 인덱스 기준으로 첫 최대값부터, 이동가능한 거리까지의 각 최대값을 비교해서 최종 x가 남는다.
    # 세로 방향 탐색
    y = 1
    for i in range(n-3) :
        for j in range(n) :
            y = max(y,s[i][j]*s[i+1][j]*s[i+2][j]*s[i+3][j])
    # 좌상단->우하단 대각선 방향 탐색
    xy = 1
    for i in range(n-3) :
        for j in range(n-3) :
            xy = max(xy,s[i][j]*s[i+1][j+1]*s[i+2][j+2]*s[i+3][j+3])
    # 우상단 -> 좌하단 대각선 방향 탐색
    yx = 1
    for i in range(n-3) :
        for j in range(3,n) :
            yx = max(yx,s[i][j]*s[i+1][j-1]*s[i+2][j-2]*s[i+3][j-3])
            
    print(max(x,y,xy,yx))

if __name__ == "__main__" :
    n = int(input())
    s = [[int(x) for x in input().split()] for y in range(n)]
    main(s)