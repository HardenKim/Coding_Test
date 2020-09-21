"""
url : https://www.acmicpc.net/problem/14888
problem : 연산자 끼워넣기
algorithm : 브루트 포스
date : 2020.09.20
"""
N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1e9, 1e9 # 십억

def solution():
    
    def bf(idx, val, add, sub, mul, div):
        global mx, mn
        if idx == N:
            mx = max(mx, val)
            mn = min(mn, val)
            return
        if add:
            bf(idx+1, val+A[idx], add-1, sub, mul, div)
        if sub:
            bf(idx+1, val-A[idx], add, sub-1, mul, div)
        if mul:
            bf(idx+1, val*A[idx], add, sub, mul-1, div)
        if div:
            bf(idx+1, val//A[idx] if val >= 0 else -((-val)//A[idx]), add, sub, mul, div-1)

    bf(1, A[0], op[0], op[1], op[2], op[3])
    print(mx)
    print(mn)

solution()