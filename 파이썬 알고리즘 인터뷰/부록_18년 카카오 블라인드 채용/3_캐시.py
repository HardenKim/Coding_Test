import collections
from typing import List

# deque : 배열 크기 정하고, 교체 방식은 LRU 

def solution(cacheSize: int, cities: List[str]) -> int:
    elapsed: int = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()
        # 캐시 히트 시 재삽입 처리
        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else:  # 캐시 미스 시 삽입만
            cache.append(c)
            elapsed += 5
    return elapsed
