"""
url : https://www.acmicpc.net/problem/17143
problem : 낚시왕
algorithm : 시뮬레이션
date : 2020.10.04
"""
R, C, M = map(int, input().split())
a = [[0] * C for _ in range(R)]
que = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    a[r-1][c-1] = [s, d, z]
    que.append([r-1, c-1])

di = [[-1,0],[1,0],[0,1],[0,-1]]

def solution():
    global a, que
    ret, pi, pj = 0, -1, -1

    def direction(d):
        if d == 1: return 2
        elif d == 2: return 1
        elif d == 3: return 4
        else: return 3

    for col in range(C):
        # fishing
        for i in range(R):
            if a[i][col]:
                ret += a[i][col][2]
                a[i][col] = 0
                pi, pj = i, col
                break
        # moving
        arr = [[0] * C for _ in range(R)]
        que2 = []
        for i, j in que:
            if i == pi and j == pj:
                continue
            s, d, z = a[i][j][0], a[i][j][1], a[i][j][2]
            if d < 3:
                ni, nj = i + s * di[d-1][0], j
                if not 0 <= ni < R:
                    temp = s
                    if d == 1:
                        s -= i
                        i = 0
                    else:
                        s -= R-1 - i
                        i = R-1
                    d = direction(d)
                    xx, yy = divmod(s, R-1)
                    if xx % 2 == 0:
                        if i == 0:
                            ni = yy
                        else:
                            ni = R-1 - yy
                    else:
                        if i == 0:
                            ni = R-1 - yy
                        else:
                            ni = yy
                        d = direction(d)
                    s = temp
            else:
                ni, nj = i, j + s * di[d-1][1]
                if not 0 <= nj < C:
                    temp = s
                    if d == 3:
                        s -= C-1 - j
                        j = C-1
                    else:
                        s -= j
                        j = 0
                    d = direction(d)
                    xx, yy = divmod(s, C-1)
                    if xx % 2 == 0:
                        if j == 0:
                            nj = yy
                        else:
                            nj = C-1 - yy
                    else:
                        if j == 0:
                            nj = C-1 - yy
                        else:
                            nj = yy
                        d = direction(d)
                    s = temp
            if arr[ni][nj]:
                if z > arr[ni][nj][2]:
                    arr[ni][nj] = [s, d, z]
            else:
                arr[ni][nj] = [s, d, z]
                que2.append([ni, nj])
        a = arr
        que = que2
    return ret                    
print(solution())
