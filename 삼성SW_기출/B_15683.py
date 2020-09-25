"""
url : https://www.acmicpc.net/problem/15683
problem : 감시
algorithm : 브루트 포스
date : 2020.09.22
"""
N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
D = { # 상하좌우
    1:[(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)],
    2:[(1,1,0,0), (0,0,1,1)],
    3:[(1,0,1,0), (1,0,0,1), (0,1,1,0), (0,1,0,1)],
    4:[(1,1,1,0), (1,1,0,1), (1,0,1,1), (0,1,1,1)],
    5:[(1,1,1,1)]
}
mn = float('inf')
empty = 0
def solution():
    global mn, empty
    cctv = []
    for i in range(N):
        for j in range(M):
            if B[i][j] == 0:
                empty += 1
            if B[i][j]%6 != 0:
                cctv.append((i,j,B[i][j]))
    if not cctv : 
        return empty
    print(cctv)
    def observe(x,y,u,d,l,r):
        arr = set()
        if u:
            nx = x
            while nx-1 >= 0:
                if B[nx-1][y] == 0:
                    arr.add((nx-1,y))
                    nx -= 1
                elif B[nx-1][y] != 6:
                    nx -= 1
                else:
                    break
        if d:
            nx = x
            while nx+1 < N:
                if B[nx+1][y] == 0:
                    arr.add((nx+1,y))
                    nx += 1
                elif B[nx+1][y] != 6:
                    nx += 1
                else:
                    break
        if l:
            ny = y
            while ny-1 >= 0:
                if B[x][ny-1] == 0:
                    arr.add((x,ny-1))
                    ny -= 1
                elif B[x][ny-1] != 6:
                    ny -= 1
                else:
                    break
        if r:
            ny = y
            while ny+1 < M:
                if B[x][ny+1] == 0:
                    arr.add((x,ny+1))
                    ny += 1
                elif B[x][ny+1] != 6:
                    ny += 1
                else:
                    break
        return arr

    def bp(idx, arr):
        global mn, empty
        if idx == len(cctv):
            mn = min(mn, empty-len(arr))
            return
        x, y, d = cctv[idx][0], cctv[idx][1], cctv[idx][2]
        for u,d,l,r in D[d]:
            arr2 = observe(x,y,u,d,l,r)
            bp(idx+1, arr|arr2)

    bp(0,set())
    return mn

print(solution())