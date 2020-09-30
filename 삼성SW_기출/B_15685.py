"""
url : https://www.acmicpc.net/problem/15685
problem : 드래곤 커브
algorithm : 브루트 포스
date : 2020.09.22
"""
v, ans = [0], 0
a = [[0]*101 for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

for i in range(1, 11):
    k = 1<<(i-1)
    for j in range(k):
        v.append((v[k-j-1]+1)%4)

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    for i in range(1<<g):
        x, y = x+dx[(v[i]+d)%4], y+dy[(v[i]+d)%4]
        a[x][y] = 1

for i in range(100):
    for j in range(100):
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
            ans += 1
print(ans)

