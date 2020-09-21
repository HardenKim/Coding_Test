"""
url : https://www.acmicpc.net/problem/14890
problem : 경사로
algorithm : 시뮬레이션
date : 2020.09.20
"""
N, L = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ret = 0
def solution():
    global ret
    def slope(i, d):
        global ret
        cnt = 1
        for j in range(N-1):
            
            v = arr[i][j+1] - arr[i][j] if d else arr[j+1][i] - arr[j][i]
            if v == 0:
                cnt += 1
            elif v == 1 and cnt >= L:
                cnt = 1
            elif v == -1 and cnt >= 0:
                cnt = 1-L
            else:
                return
        if cnt >= 0:
            ret += 1

    for i in range(N):
        slope(i, 1)
        slope(i, 0)
    return ret

print(solution())
