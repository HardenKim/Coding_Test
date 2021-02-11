"""
url : https://www.acmicpc.net/problem/15686
problem : 치킨 배달
algorithm : 브루트 포스
date : 2020.09.30
"""
N, M= map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
home, chicken, v = [], [], []
ret = float('inf')

def solution():

    def dfs(idx, cnt):
        global ret
        if idx > len(chicken):
            return
        if cnt == M:
            val = 0
            for hx, hy in home:
                d = float('inf')
                for i in v: # 집과 가장 가까운 치킨집과의 치킨 거리 구하기
                    cx, cy = chicken[i]
                    d = min(d, abs(hx - cx) + abs(hy - cy))
                val += d # 각 집의 치킨 거리 더하기
            ret = min(ret, val) 
            return

        # v는 유효한 치킨집의 인덱스
        v.append(idx) # 현재 치킨집 포함 O
        dfs(idx+1, cnt+1) 
        v.pop() #현재 치킨집 포함 X
        dfs(idx+1, cnt) 

    # 1. 집과 치킨집 위치 찾기
    for i in range(N):
        for j in range(N):
            if B[i][j] == 1:
                home.append((i+1,j+1))
            elif B[i][j] == 2:
                chicken.append((i+1,j+1))

    dfs(0, 0)
    return ret

print(solution())