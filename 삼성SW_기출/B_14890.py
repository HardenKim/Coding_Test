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
        cnt = 1 # 연속된 칸의 개수
        for j in range(N-1):
            
            v = arr[i][j+1] - arr[i][j] if d else arr[j+1][i] - arr[j][i]
            if v == 0:
                cnt += 1
            elif v == 1 and cnt >= L: # 오르막은 낮은 칸이 L개 이상인지 바로 확인 가능
                cnt = 1 # L개 이상이면 연속된 칸의 개수를 1로 초기화
            elif v == -1 and cnt >= 0: # 내리막은 낮은 칸의 개수를 바로 확인 불가능
                cnt = 1-L # 내리막 초반에 연속된 칸의 개수를 음수로 변경
            else:
                return
        if cnt >= 0:
            ret += 1

    for i in range(N):
        slope(i, 1)
        slope(i, 0)
    return ret

print(solution())