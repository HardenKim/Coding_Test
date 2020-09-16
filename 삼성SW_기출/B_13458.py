"""
url : https://www.acmicpc.net/problem/13458
problem : 시험 감독
algorithm : 수학
"""

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    ret = 0

    for i in range(N):
        if A[i] > B:
            div, mod = divmod((A[i]-B), C)
            if mod == 0:
                ret += div+1
            else:
                ret += div+2
        else:
            ret += 1
    return ret

print(solution())
