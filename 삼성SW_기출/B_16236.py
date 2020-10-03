"""
url : https://www.acmicpc.net/problem/16236
problem : 아기 상어
algorithm : BFS
date : 2020.10.03
"""
import heapq
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
di = [[-1,0], [1,0], [0,-1], [0,1]]

def solution():
    heap = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 9:
                heapq.heappush(heap, (0, i, j))
                A[i][j] = 0

    body, eat, ret = 2, 0, 0
    check = [[False] * N for _ in range(N)]
    while heap:
        d, x, y = heapq.heappop(heap)
        if 0 <  A[x][y] < body:
            eat += 1
            A[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ret += d
            d = 0
            while heap:
                heap.pop()
            check = [[False] * N for _ in range(N)]
        for dx, dy in di:
            nd, nx, ny = d+1, x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if check[nx][ny] or A[nx][ny] > body:
                continue
            check[nx][ny] = True
            heapq.heappush(heap, (nd, nx, ny))
    
    return ret
    
print(solution())
