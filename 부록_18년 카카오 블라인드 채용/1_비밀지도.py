from typing import List

# 비트 연산 bin()
# 배열 zfill()

def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps = []
    for i in range(n):
        # OR 연산 후 이진수 변환
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
        )
    return maps
