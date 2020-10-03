"""
url : https://www.acmicpc.net/problem/16235
problem : 나무 재테크
algorithm : 시뮬레이션
date : 2020.10.02
"""
from collections import deque
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
ground = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

di = [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]

def solution():

    for _ in range(K):
        # 봄
        for i in range(N):
            for j in range(N):
                if len(tree[i][j]) <= 0:
                    continue
                tree[i][j].sort()
                for idx in range(len(tree[i][j])):
                    if tree[i][j][idx] <= ground[i][j]:
                        tree[i][j][idx] += 1
                        ground[i][j] -= tree[i][j][idx]
                    else:
                        die = tree[i][j][idx:]
                        # 여름
                        for now in die:
                            ground[i][j] += now // 2
                        tree[i][j] = tree[i][j][:idx]
                        break
        # 가을
        for i in range(N):
            for j in range(N):
                c = 0
                if tree[i][j]:
                    for now in tree[i][j]:
                        if now % 5 == 0:
                            c += 1
                if c > 0:
                    for k in range(8):
                        ni = i + di[i][0]
                        nj = j + di[i][1]
                        if 0 <= ni < N and 0 <= nj < N:
                            for _ in range(c):
                                tree[ni][nj].append(1)
        # 겨울
        for i in range(N):
            for j in range(N):
                ground[i][j] += A[i][j]

    ret = 0
    for i in range(N):
        for j in range(N):
            ret += len(tree[i][j])    
    return ret
print(solution())