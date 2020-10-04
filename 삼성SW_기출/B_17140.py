"""
url : https://www.acmicpc.net/problem/17140
problem : 이차원 배열과 연산
algorithm : 시뮬레이션
date : 2020.10.04
"""
from collections import Counter
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def solution():
    global A, k, r, c
    ret = 0
    while ret <= 100:
        row, col = len(A), len(A[0])
        if row >= r and col >= c:
            if A[r-1][c-1] == k:
                return ret
        
        if row >= col:
            arr = [[] for _ in range(row)]
            maxlen = 0
            for i in range(row):
                for key, value in sorted(Counter(A[i]).items(), key = (lambda x: (x[1], x[0]))):
                    if key == 0:
                        continue
                    arr[i].extend([key, value])
                maxlen = max(maxlen, len(arr[i]))
            for i in range(row):
                leng = maxlen - len(arr[i])
                arr[i].extend([0]*leng)
        else:
            arr = [[] for _ in range(col)]
            maxlen = 0
            A = [list(x) for x in zip(*A)]
            for i in range(col):
                for key, value in sorted(Counter(A[i]).items(), key = (lambda x: (x[1], x[0]))):
                    if key == 0:
                        continue
                    arr[i].extend([key, value])
                maxlen = max(maxlen, len(arr[i]))
            for i in range(col):
                leng = maxlen - len(arr[i])
                arr[i].extend([0]*leng)
            arr = [list(x) for x in zip(*arr)]
        A = arr[:]                  
        ret += 1
    return -1                  
print(solution())
