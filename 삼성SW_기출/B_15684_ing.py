"""
url : https://www.acmicpc.net/problem/15684
problem : 사다리 조작
algorithm : 브루트 포스
date : 2020.09.22

구현중... ㅠ
"""
N, M, H = map(int, input().split())
B = [[0]*M for _ in range(N)]
for i in range(H):
    x,y = map(int, input().split())
    B[x-1][y-1] = 1

def solution():
    

print(solution())


"""

    1   2
1   | - |
2   |   |
3   |   |