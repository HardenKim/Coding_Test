"""
url : https://www.acmicpc.net/problem/14891
problem : 톱니바퀴
algorithm : 시뮬레이션
date : 2020.09.21
"""
T = [list(map(int, input().strip())) for _ in range(4)]
K  = int(input())
R = [list(map(int, input().split())) for _ in range(K)]

def solution():
    ret = 0

    def rotate(i, r):
        if r == 1: # 시계
            tmp = T[i-1][-1]
            for j in range(8):
                T[i-1][j], tmp = tmp, T[i-1][j]
        else:    # 반시계
            tmp = T[i-1][0]
            for j in range(7, -1, -1):
                T[i-1][j], tmp = tmp, T[i-1][j]
        

    for i, r in R:
        arr = [(i,r)]
        # 오른쪽
        ni, nr = i, r
        while ni < 4:
            if T[ni-1][2] != T[ni][6]:
                nr = -nr
                ni += 1
                arr.append((ni, nr))
            else:
                break
        # 왼쪽
        ni, nr = i, r
        while ni > 1:
            if T[ni-1][6] != T[ni-2][2]:
                nr = -nr
                ni -= 1
                arr.append((ni, nr))
            else:
                break
        # 회전
        for a, b in arr:
            rotate(a,b)
    
    for i in range(4):
        if T[i][0] == 1:
            ret += 2**i

    return ret

print(solution())