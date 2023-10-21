from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        n  = len(s) # n = 6
        frequencies = Counter(s) # {e: 1, b: 2, c: 3}
        buckets = [[] for _ in range(n + 1)] # [[], [], [], [], [], [], []]

        for c, f in frequencies.items():
            buckets[f].append(c) # [[], [e], [b], [c], [], [], []]

        result = ''

        for f in range(n, 0, -1): # counting backwards from n to 1
            for char in buckets[f]:
                result += f * char
                # f = n = 6 --> nothing
                # f = 5 --> nothing
                # f = 4 --> nothing
                # f = 3 --> 3 * 'c' --> 'ccc'
                # f = 2 --> 2 * 'b' --> 'cccbb'
                # f = 1 --> 1 * 'e' --> 'cccbbe'

        return result
