"""
url : https://www.acmicpc.net/problem/14501
problem : 퇴사
algorithm : DP, DFS
date : 2020.09.17
"""

def solution(): 
    N = int(input()) 
    L = [list(map(int, input().split())) for _ in range(N)]
    dp = [0]*N

    for i in range(N):
        if i + L[i][0] <= N:
            dp[i] = L[i][1]
            for j in range(i):
                if j + L[j][0] <= i:
                    dp[i] = max(dp[i], dp[j]+L[i][1])
                print(dp)
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