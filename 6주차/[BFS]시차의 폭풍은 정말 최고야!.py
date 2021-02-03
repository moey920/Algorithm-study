from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1 ,2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
 
def bfs(Xs, Ys, Xg, Yg):
    q = deque()
    q.append([Xs, Ys])
    chess_map[Xs][Ys]=1
    while q:
        
        xi, yi = q.popleft()

        if xi==Xg and yi==Yg:
            return chess_map[xi][yi]-1

        for i in range(8):
            next_x = xi +dx[i]
            next_y = yi +dy[i]
            if 0<=next_x <l and 0<=next_y<l:
                if chess_map[next_x][next_y]==0:
                    q.append((next_x, next_y))
                    chess_map[next_x][next_y]= chess_map[xi][yi]+1



l = int(input())
Xs, Ys = map(int, input().split())
Xg, Yg = map(int, input().split())
chess_map = [[0]*l for _ in range(l)]
print(bfs(Xs, Ys, Xg, Yg))





