"""
url : https://www.acmicpc.net/problem/17142
problem : 연구소 3
algorithm : BFS
date : 2020.10.05
"""
from collections import deque
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
selceted = [False] * 10
dx , dy = [1, -1, 0, 0], [0, 0, 1, -1]
que, virus, vacnt, ret = deque(), [], 0, float('inf')

def solution():
    global virus, vacnt, ret

    def bfs(arr):
        global ret
        infect, times = 0, 0
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if A[nx][ny] != 1 and arr[nx][ny] == -1:
                    arr[nx][ny] = arr[x][y] + 1
                    que.append((nx,ny))
                    if A[nx][ny] == 0:
                        infect += 1
                        times = arr[nx][ny]
        if infect == vacnt:
            ret = min(ret, times)

    def solve(idx, cnt, v):
        global que
        if cnt == M:
            arr = [[-1] * N for _ in range(N)]
            for i in range(v):
                if selceted[i]:
                    x, y = virus[i]
                    que.append((x, y))
                    arr[x][y] = 0
            bfs(arr)
            return
        for i in range(idx, v):
            if not selceted[i]:
                selceted[i] = True
                solve(i+1, cnt+1, v)
                selceted[i] = False

    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                virus.append([i,j])
            elif A[i][j] == 0:
                vacnt += 1
    
    solve(0,0,len(virus))
    
    if ret == float('inf'):
        return -1
    return ret     
print(solution())