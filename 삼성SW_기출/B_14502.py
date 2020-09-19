"""
url : https://www.acmicpc.net/problem/14502
problem : 연구소
algorithm : 브루트 포스 , DFS
date : 2020.09.18
"""
import copy
minVal, carr = float('inf'), []
def solution():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    room, virus_arr = 0, []    
    global minVal, carr

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus_arr.append((i,j))
            if arr[i][j] != 1:
                room += 1

    def dfs(x,y):
        global minVal, carr
        ret = 1
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if carr[nx][ny] == 0:
                carr[nx][ny] = 2
                ret += dfs(nx,ny)
        return ret

    def solve(wall, x, y):
        global minVal, carr
        if wall == 3:
            carr = copy.deepcopy(arr)
            val = 0
            for vx, vy in virus_arr:
                val += dfs(vx, vy)
            minVal = min(minVal, val)
            return
        
        for i in range(x, N):
            k = y if i == x else 0
            for j in range(k,M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    solve(wall+1, i, j+1)
                    arr[i][j] = 0

    solve(0,0,0)
    return room - minVal - 3

print(solution())