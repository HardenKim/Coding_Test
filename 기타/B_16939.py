"""
url : https://www.acmicpc.net/problem/16939
problem : 2X2X2 큐브
algorithm : 시뮬레이션
date : 2020.09.30

* 큐빙을 풀기 전에 풀면 좋은 문제
"""
import copy
def solution():
    def check():
        idx = 1
        while idx < len(c):
            for i in range(idx+1, idx+4):
                if c[idx] != c[i]:
                    return False
            idx += 4
        return True
    def one(c):
        temp1, temp2 = c[21], c[23];
        c[21] = c[4]
        c[23] = c[2]
        c[4] = c[8]
        c[2] = c[6]
        c[6] = c[10]
        c[8] = c[12]
        c[12] = temp1
        c[10] = temp2
    def reone(c):
        one(c)
        one(c)
        one(c)
    def two(c):
        temp1, temp2 = c[22], c[24];
        c[22] = c[3]
        c[24] = c[1]
        c[3] = c[7]
        c[1] = c[5]
        c[7] = c[11]
        c[5] = c[9]
        c[11] = temp1
        c[9] = temp2
    def retwo(c):
        two(c)
        two(c)
        two(c)
    def three(c):
        temp1, temp2= c[11], c[12]
        c[11] = c[13]
        c[12] = c[15]
        c[13] = c[2]
        c[15] = c[1]
        c[2] = c[20]
        c[1] = c[18]
        c[20] = temp1
        c[18] = temp2    
    def rethree(c):
        three(c)
        three(c)
        three(c)
    def four(c):
        temp1, temp2 = c[9], c[10];
        c[9] = c[14]
        c[10] = c[16]
        c[14] = c[4]
        c[16] = c[3]
        c[4] = c[19]
        c[3] = c[17]
        c[19] = temp1
        c[17] = temp2
    def refour(c):
        four(c)
        four(c)
        four(c)    
    def five(c):
        temp1, temp2 = c[19], c[20]
        c[20] = c[24]
        c[19] = c[23]
        c[24] = c[16]
        c[23] = c[15]
        c[16] = c[8]
        c[15] = c[7]
        c[8] = temp2
        c[7] = temp1
    def refive(c):
        five(c)
        five(c)
        five(c)
    def six(c):
        temp1, temp2 = c[18], c[17];
        c[18] = c[22]
        c[17] = c[21]
        c[22] = c[14]   
        c[21] = c[13]   
        c[13] = c[5]
        c[14] = c[6]
        c[5] = temp2
        c[6] = temp1
    def resix(c):
        six(c)
        six(c)
        six(c)

    cube = [0] + list(map(int, input().split()))
    # one
    c = copy.copy(cube)
    one(c)
    if check(c):
        return True
    one(c)
    one(c)
    if check(c):
        return True
    # two
    c = copy.copy(cube)
    two(c)
    if check(c):
        return True
    two(c)
    two(c)
    if check(c):
        return True
    # three
    c = copy.copy(cube)
    three(c)
    if check(c):
        return True
    three(c)
    three(c)
    if check(c):
        return True
    # four
    c = copy.copy(cube)
    four(c)
    if check(c):
        return True
    four(c)
    four(c)
    if check(c):
        return True
    # five
    c = copy.copy(cube)
    five(c)
    if check(c):
        return True
    five(c)
    five(c)
    if check(c):
        return True
    # six
    c = copy.copy(cube)
    six(c)
    if check(c):
        return True
    six(c)
    six(c)
    if check(c):
        return True
    
    return False

print(solution())