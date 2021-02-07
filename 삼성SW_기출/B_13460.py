"""
url : https://www.acmicpc.net/problem/13460
problem : 구슬탈출2
algorithm : 구현, 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색
"""
from collections import deque

def solution():
    N, M = map(int, input().split())
    B = [list(input().strip()) for _ in range(N)]
    dx, dy = [-1,1,0,0] ,[0,0,-1,1]
    que = deque() # BFS : queue 활용
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    def init(): # 초기 구슬의 좌표를 큐에 저장
        rx, ry, bx, by = 0, 0, 0, 0
        for i in range(N):
            for j in range(M):
                if B[i][j] == 'R':
                    rx, ry = i, j
                elif B[i][j] == 'B':
                    bx, by = i, j
        que.append((rx,ry,bx,by, 1)) # 구슬의 위치와 depth 저장
        visited[rx][ry][bx][by] = True

    def move(x, y, dx, dy):
        cnt = 0 # 이동한 칸 수
        while B[x+dx][y+dy] != '#' and B[x][y] != 'O': # 다음이 벽이 아니거나 현재가 구멍이 아닐 때 까지
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
        
            for i in range(4): # 4방향
                nrx, nry, nrc = move(rx, ry, dx[i], dy[i])
                nbx, nby, nbc = move(bx, by, dx[i], dy[i])
                if B[nbx][nby] != 'O':
                    if B[nrx][nry] == 'O':
                        return cnt # 빨간 구슬만 구멍일 때
                    if nrx == nbx and nry == nby: # 두 구슬의 위치가 같을 때 depth가 높은 걸 뒤로 이동
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
