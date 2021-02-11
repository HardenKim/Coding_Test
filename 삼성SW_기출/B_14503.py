"""
url : https://www.acmicpc.net/problem/14503
problem : 로봇 청소기
algorithm : 시뮬레이션
date : 2020.09.19
"""

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
D = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} # 북동남서
cnt = 1
def solution():
    global cnt
    def dfs(x, y, d):
        global board, N, M, D, cnt
        for _ in range(4):
            d = (d+3) % 4 # 왼쪽으로 이동하기 위해 +3
            nx = x + D[d][0]
            ny = y + D[d][1]
            if not board[nx][ny]: # 빈 칸일 때
                board[nx][ny] = 2 # 2로 변경 (청소)
                cnt += 1
                dfs(nx, ny, d)
                return
        if board[x-D[d][0]][y-D[d][1]] == 1: # 뒤가 벽일 경우
            return
        else:
            dfs(x-D[d][0], y-D[d][1], d) # 뒤가 빈 칸일 경우

    board[x][y] = 2 # 처음 현재 칸 청소
    dfs(x,y,d)
    return cnt
    
print(solution())