"""
url : https://www.acmicpc.net/problem/16235
problem : 나무 재테크
algorithm : 시뮬레이션
date : 2020.10.02
"""
from collections import deque, defaultdict
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
arr = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1][z] += 1

d = [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]

def solution():
    ret = 0

    def solve():
        global tree, arr, A
        temp = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if not tree[x][y]: # 나무가 없는 경우
                    arr[x][y] += A[x][y] # 양분 추가
                    continue
                die, spread = 0, 0
                # 봄, 여름
                for age, num in sorted(tree[x][y].items()): # 나무 나이와 개수를 나이가 낮은 순서부터 추출
                    cnt = arr[x][y] // age
                    if cnt >= num:
                        arr[x][y] -= age * num
                        temp[x][y][age+1] += num
                        if (age+1) % 5 == 0:
                            spread += num
                    elif 1 <= cnt < num:
                        arr[x][y] -= age * cnt
                        temp[x][y][age+1] += cnt
                        die += (age//2) * (num-cnt)
                        if (age+1) % 5 == 0:
                            spread += cnt
                    else:
                        die += (age//2) * num
                # 가을
                if spread != 0:
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            temp[nx][ny][1] += spread
                # 겨울
                arr[x][y] += A[x][y] + die
        return temp
    
    for _ in range(K):
        global tree
        tree = solve()

    for x in range(N):
        for y in range(N):
            ret += sum(tree[x][y].values())

    return ret

print(solution())


