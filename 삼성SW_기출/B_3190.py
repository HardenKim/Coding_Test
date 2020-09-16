"""
url : https://www.acmicpc.net/problem/3190
problem : 뱀
algorithm : 시뮬레이션
"""

from collections import deque
def solution():
    # 보드와 방향
    N = int(input())
    K = int(input())
    B = [['#']*(N+2)] + [['#'] + ['0']*N + ['#'] for _ in range(N)] + [['#']*(N+2)]
    for i in range(K):
        x, y = map(int, input().split())
        B[x][y] = '*'
    L = int(input())
    L_dic = {}
    for i in range(L):
        k, v = input().split()
        L_dic[int(k)] = v
    
    time = 0
    x,y = 1,1
    D = {0:(0,1), 1:(-1,0), 2:(-0,-1), 3:(1,0)} # 동북서남
    d = 0 # 동
    que = deque()
    que.append((x,y))    
    B[x][y] = '1'
    
    while True:
        x += D[d][0]
        y += D[d][1]
        time += 1
        
        # 벽일 경우
        if B[x][y] == '#' or B[x][y] == '1':
            return time
        # 사과일 경우 
        elif B[x][y] == '*':
            que.append((x,y))
            B[x][y] = '1'
        # 빈공간일 경우
        else:
            B[x][y] = '1'
            que.append((x,y))
            dx, dy = que.popleft()
            B[dx][dy] = '0'
        
        # 방향이 바뀔 때
        if time in L_dic:        
            if L_dic[time] == 'D':
                d -= 1
                if d == -1: d = 3
            else:
                d += 1
                if d == 4: d = 0

    return time

print(solution())
