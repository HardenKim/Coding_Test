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
        if cnt == N//2: # True 팀이 2/N이면 능력치 계산
            val = 0
            for i in range(N):
                for j in range(i+1, N): # range(N) -> range(i+1, N) 을 통해 반복횟수를 줄인다
                    if T[i] and T[j]: # 반복횟수를 줄이기 위해 두 선수의 능력치 한번에 계산
                        val += S[i][j] 
                        val += S[j][i] 
                    if not T[i] and not T[j]:
                        val -= S[i][j]
                        val -= S[j][i]
            mn = min(mn, abs(val))
            return

        T[idx] = True # 이 선수가 True 팀일 경우
        team(cnt+1, idx+1) # cnt 는 True 팀의 인원
        T[idx] = False # 이 선수가 False 팀일 경우
        team(cnt, idx+1)

    team(0, 0)
    return mn

print(solution())