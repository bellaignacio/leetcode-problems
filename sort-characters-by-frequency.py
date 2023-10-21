# from collections import defaultdict
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # frequencies = defaultdict(int)
        # for c in s:
        #     frequencies[c] += 1

        n  = len(s)
        frequencies = Counter(s)
        bucket = [[] for _ in range(n + 1)]

        for c, f in frequencies.items():
            bucket[f].append(c)

        result = ''

        for f in range(n, 0, -1):
            for char in bucket[f]:
                result += f * char

        return result
