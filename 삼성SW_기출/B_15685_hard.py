"""
url : https://www.acmicpc.net/problem/15685
problem : 드래곤 커브
algorithm : 시뮬레이션
date : 2020.09.22
"""
B = [[0]*101 for _ in range(101)]
D = {0:(1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)} # 우, 상, 좌, 하
G = [0]
ret = 0

for i in range(1,11):
    k = 1<<(i-1)
    for j in range(k):
        G.append((G[k-j-1]+1)%4)
    
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    B[x][y] = 1
    for i in range(1<<g):
        x, y = x + D[(G[i]+d)%4][0], y + D[(G[i]+d)%4][1]
        B[x][y] = 1

for i in range(100):
    for j in range(100):
        if B[i][j] and B[i+1][j] and B[i][j+1] and B[i+1][j+1]:
            ret += 1
print(ret)

