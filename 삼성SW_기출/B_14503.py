"""
url : https://www.acmicpc.net/problem/14503
problem : 로봇 청소기
algorithm : 시뮬레이션
date : 2020.09.19
"""

N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
cnt = 1
def solution():
    global cnt
    def dfs(x, y, d):
        global arr, N, M, D, cnt
        for _ in range(4):
            d = (d+3) % 4
            nx = x + D[d][0]
            ny = y + D[d][1]
            if not arr[nx][ny]:
                arr[nx][ny] = 2
                cnt += 1
                dfs(nx, ny, d)
                return
        if arr[x-D[d][0]][y-D[d][1]] == 1:
            return
        else:
            dfs(x-D[d][0], y-D[d][1], d)

    arr[x][y] = 2
    dfs(x,y,d)
    return cnt
    
print(solution())