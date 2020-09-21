"""
url : https://www.acmicpc.net/problem/14889
problem : 스타트와 링크
algorithm : 브루트 포스
date : 2020.09.20
"""
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
T = [False] * N
mn = float('inf')
def solution():
    global mn

    def team(cnt, idx):
        global T, mn
        if idx == N:
            return
        if cnt == N//2:
            val = 0
            for i in range(N):
                for j in range(N):
                    if T[i] and T[j]:
                        val += S[i][j]
                    if not T[i] and not T[j]:
                        val -= S[i][j]
            mn = min(mn, abs(val))
            return

        T[idx] = True
        team(cnt+1, idx+1)
        T[idx] = False
        team(cnt, idx+1)

    team(0, 0)
    return mn
print(solution())