import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]

# 내 풀이
# from collections import defaultdict
# import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = re.sub(r'[^\w]', ' ', paragraph).lower().split()
#         dic = defaultdict(int)
#         for w in words:
#             if w not in banned:
#                 dic[w] += 1

#         return max(dic.keys(), key=(lambda k: dic[k]))