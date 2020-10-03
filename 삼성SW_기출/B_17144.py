"""
url : https://www.acmicpc.net/problem/17144
problem : 미세먼지 안녕!
algorithm : 시뮬레이션
date : 2020.10.03
"""
import heapq
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
di = [[-1,0], [1,0], [0,-1], [0,1]]
S1, S2 = -1, 0
def solution():
    global S1, S2
    def diffuse():
        global A
        arr = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if A[i][j] >= 5:
                    d = A[i][j] // 5
                    for dx, dy in di:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                            arr[nx][ny] += d
                            A[i][j] -= d
        for i in range(R):
            for j in range(C):
                A[i][j] += arr[i][j]

    def purify():
        global S1, S2, A
        for i in range(S1-2, -1,-1):
            A[i+1][0] = A[i][0]
        for i in range(C-1):
            A[0][i] = A[0][i+1]
        for i in range(S1):
            A[i][C-1] = A[i+1][C-1]
        for i in range(C-2, -1, -1):
            A[S1][i+1] = A[S1][i]
        A[S1][1] = 0
        for i in range(S2+1, R-1):
            A[i][0] = A[i+1][0]
        for i in range(C-1):
            A[R-1][i] = A[R-1][i+1]
        for i in range(R-2, S2-1, -1):
            A[i+1][C-1] = A[i][C-1]
        for i in range(C-2, -1, -1):
            A[S2][i+1] = A[S2][i]
        A[S2][1] = 0


    for i in range(R):
        for j in range(C):
            if A[i][j] == -1:
                if S1 == -1:
                    S1 = i
                else:
                    S2 = i
    
    for i in range(T):
        diffuse()
        purify()
    

    return sum(map(sum, A)) + 2
    
print(solution())
