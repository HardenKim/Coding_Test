"""
url : https://www.acmicpc.net/problem/14501
problem : 퇴사
algorithm : DP, DFS
date : 2020.09.17
"""

def solution(): 
    N = int(input()) 
    L = [list(map(int, input().split())) for _ in range(N)]
    dp = [0]*N # N일 동안 선택할 수 있는 최대 금액

    for i in range(N):
        if i + L[i][0] <= N: # 퇴사 전에 가능한 상담일 경우
            dp[i] = L[i][1] # 당일 상담의 금액을 저장
            for j in range(i):
                if j + L[j][0] <= i: # 이전의 상담이 오늘 전에 가능할 경우
                    dp[i] = max(dp[i], dp[j]+L[i][1]) # (이전의 상담 금액 + 당일 상담 금액)의 최대 값 선택
    return max(dp)
print(solution())

""" dfs(i) = max(dfs(i+1), dfs(i+T[i])+P[i]) """ 
"""
from collections import defaultdict
ret = 0
def solution():
    N = int(input()) 
    L = [list(map(int, input().split())) for _ in range(N)]
    dp = defaultdict(int)

    def dfs(day):
        # print("day : " +str(day))
        if day == N:
            return 0
        if day > N:
            return -float('inf')
        if day in dp:
            return dp[day]
        ret = max(dfs(day+1), dfs(day+L[day][0])+L[day][1])
            
        dp[day] = ret
        return ret
    
    dfs(0)
    return dp[0]
print(solution())
"""