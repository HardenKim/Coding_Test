"""
url : https://www.acmicpc.net/problem/14500
problem : 테트로미노
algorithm : 브루트 포스
date : 2020.09.17
"""
ret = 0
def solution(): 
    N, M = map(int, input().split()) 
    B = [list(map(int, input().split())) for _ in range(N)]
    T = [ 
        [0,1,4,5],                                  # ㅁ
        [0,1,2,3], [0,4,8,12],                      # -
        [0,4,5,9], [1,4,5,8], [1,2,4,5], [0,1,5,6], # Z
        [0,1,2,5], [1,4,5,6], [0,4,5,8], [1,4,5,9], # ㅗ
        [0,4,8,9], [1,5,8,9], [0,1,2,4], [0,4,5,6], # ㄴ
        [0,1,5,9], [0,1,4,8], [2,4,5,6], [0,1,2,6] 
        ] 
    T = [
        [[0,0], [0,1], [1,0], [1,1]], 
        [[0,0], [0,1], [0,2], [0,3]], 
        [[0,0], [1,0], [2,0], [3,0]], 
        [[0,0], [0,1], [0,2], [1,0]],
        [[0,2], [1,0], [1,1], [1,2]], 
        [[0,0], [1,0], [1,1], [1,2]], 
        [[0,0], [0,1], [0,2], [1,2]], 
        [[0,0], [1,0], [2,0], [2,1]], 
        [[0,0], [0,1], [1,1], [2,1]], 
        [[0,0], [0,1], [1,0], [2,0]], 
        [[0,1], [1,1], [2,0], [2,1]], 
        [[0,0], [1,0], [1,1], [2,1]], 
        [[0,1], [1,0], [1,1], [2,0]], 
        [[0,1], [0,2], [1,0], [1,1]], 
        [[0,0], [0,1], [1,1], [1,2]], 
        [[0,0], [0,1], [0,2], [1,1]], 
        [[0,1], [1,0], [1,1], [1,2]], 
        [[0,1], [1,0], [1,1], [2,1]],
        [[0,0], [1,0], [1,1], [2,0]] 
    ]

    # x,y 좌표
    def get_location(idx):
        location = []
        for i in range(4): 
            x, y = divmod(T[idx][i], 4) 
            location.append([x,y]) 
        return location
    # tetromino
    def tetromino(x, y): 
        global ret
        for i in range(19):
            val = 0
            # location = get_location(i)
            for j in range(4):
                try:
                    # nx = x + location[j][0]
                    # ny = y + location[j][1]
                    nx = x + T[i][j][0]
                    ny = y + T[i][j][1]
                    val += B[nx][ny]
                except IndexError:
                    break
            ret = max(ret, val)

    for i in range(N):
        for j in range(M):
            tetromino(i,j)

    return ret 

print(solution())   