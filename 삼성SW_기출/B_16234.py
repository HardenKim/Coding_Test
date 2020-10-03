"""
url : https://www.acmicpc.net/problem/16234
problem : 인구 이동
algorithm : BFS
date : 2020.10.02
* 다시 풀어보기 *
"""
from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [[-1,0], [1,0], [0,-1], [0,1]]
def solution():
    ret = 0
    def bfs(start, num):
        que = deque()
        que.append(start)
        union[start[0]][start[1]] = num
        union_sum = arr[start[0]][start[1]]
        union_cnt = 1
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx = x + di[i][0]
                ny = y + di[i][1]

                if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1 and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    union_sum += arr[nx][ny]
                    union[nx][ny] = num
                    union_cnt += 1
                    que.append([nx, ny])
        return [union_sum, union_cnt]

    while True:
        union = [[-1] * N for _ in range(N)]
        n = 0
        union_info = {}
        for i in range(N):
            for j in range(N):
                if union[i][j] == -1:
                    union_info[n] = bfs([i,j], n)
                    n += 1
        if n == N*N:    # 국경선 모두 닫힘
            break
        for i in range(N):
            for j in range(N):
                arr[i][j] = union_info[union[i][j]][0] // union_info[union[i][j]][1]
        ret += 1
    return ret
print(solution())