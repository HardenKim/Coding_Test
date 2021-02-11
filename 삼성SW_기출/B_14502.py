"""
url : https://www.acmicpc.net/problem/14502
problem : 연구소
algorithm : 브루트 포스 , DFS
date : 2020.09.18
"""
import copy
minVal, copy_board = float('inf'), []
def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    room, virus_arr = 0, []    
    global minVal, copy_board

    # 초기 바이러스와 빈칸을 저장한다.
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                virus_arr.append((i,j))
            if board[i][j] != 1:
                room += 1

    def dfs(x,y):
        global minVal, copy_board
        ret = 1 
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if copy_board[nx][ny] == 0: # 빈 칸일 경우 바이러스
                copy_board[nx][ny] = 2
                ret += dfs(nx,ny) # 바이러스 개수 추가
        return ret

    def solve(wall, x, y):
        global minVal, copy_board
        if wall == 3:
            copy_board = copy.deepcopy(board)
            val = 0
            for vx, vy in virus_arr:
                val += dfs(vx, vy) 
            minVal = min(minVal, val) # 최소 바이러스 개수
            return
        
        for i in range(x, N):
            k = y if i == x else 0
            for j in range(k,M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    solve(wall+1, i, j+1)
                    board[i][j] = 0

    solve(0,0,0)
    return room - minVal - 3 # 빈 칸 - 최소 바이러스 개수 - 벽(3개)

print(solution())


