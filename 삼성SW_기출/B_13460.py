"""
url : https://www.acmicpc.net/problem/13460
problem : 구슬탈출2
algorithm : BFS
"""
from collections import deque

def solution():
    N, M = map(int, input().split())
    B = [list(input().split()) for _ in range(N)]
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    que = deque() # BFS : queue 활용
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    def init():
        rx, ry, bx, by = 0, 0, 0, 0
        for i in range(N):
            for j in range(M):
                if B[i][j] == 'R':
                    rx, ry = i, j
                elif B[i][j] == 'B':
                    bx, by = i, j
        que.append((rx,ry,bx,by, 1))
        visited[rx][ry][bx][by] = True

    def move(x, y, dx, dy):
        cnt = 0 
        while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
            x += dx
            y += dy
            cnt += 1
        return x, y, cnt

    def solve():
        init()
        while que:
            rx, ry, bx, by, cnt = que.popleft()
            if cnt > 10:
                return -1
        
            for i in range(4):
                nrx, nry, nrc = move(rx, ry, dx[i], dy[i])
                nbx, nby, nbc = move(bx, by, dx[i], dy[i])
                if B[nbx][nby] != 'O':
                    if B[nrx][nry] == 'O':
                        return cnt
                    if nrx == nbx and nry == nby:
                        if nrc > nbc:     
                            nrx -= dx[i]
                            nry -= dy[i] 
                        else:
                            nbx -= dx[i]
                            nby -= dy[i]
                    if not visited[nrx][nry][nbx][nby]:
                        visited[nrx][nry][nbx][nby] = True
                        que.append((nrx, nry, nbx, nby, cnt+1))
        return -1

    print(solve())

solution()
