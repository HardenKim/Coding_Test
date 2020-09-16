"""
url : https://www.acmicpc.net/problem/14499
problem : 주사위 굴리기
algorithm : 시뮬레이션
"""

def solution():
    N, M, x, y, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)] # 지도
    C = list( input().split())                              # 명령
    D = {'1':(0,1), '2':(0,-1), '3':(-1,0), '4':(1,0)} # 동서북남
    Dice = [0]*6    # 0:하, 1:상, 2:동, 3:서, 4:남, 5:북

    def rotate(r):
        if r == '1':    # 동
            Dice[0],Dice[1],Dice[2],Dice[3],Dice[4],Dice[5] = Dice[2],Dice[3],Dice[1],Dice[0],Dice[4],Dice[5]
        if r == '2':    # 서
            Dice[0],Dice[1],Dice[2],Dice[3],Dice[4],Dice[5] = Dice[3],Dice[2],Dice[0],Dice[1],Dice[4],Dice[5]
        if r == '3':    # 북
            Dice[0],Dice[1],Dice[2],Dice[3],Dice[4],Dice[5] = Dice[5],Dice[4],Dice[2],Dice[3],Dice[0],Dice[1]
        if r == '4':    # 남
            Dice[0],Dice[1],Dice[2],Dice[3],Dice[4],Dice[5] = Dice[4],Dice[5],Dice[2],Dice[3],Dice[1],Dice[0]

    for i in range(K):
        x += D[C[i]][0]
        y += D[C[i]][1]
        
        if x < 0 or x >= N or y < 0 or y >= M:
            x -= D[C[i]][0]
            y -= D[C[i]][1]
            continue

        rotate(C[i])        
        if B[x][y] == 0:
            B[x][y] = Dice[0]
        else:
            Dice[0] = B[x][y]
            B[x][y] = 0
        print(Dice[1])

    return

solution()