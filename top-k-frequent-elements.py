from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) # n = 6
        counter = Counter(nums) # {1: 3, 2: 2, 3: 1}
        buckets = [[] for _ in range(n + 1)] # [[], [], [], [], [], [], []]

        for n, f in counter.items():
            buckets[f].append(n)  # [[], [3], [2], [1], [], [], []]

        result = []

        while len(result) < k:
            if buckets[-1] == []:
                buckets.pop()
            else:
                result += buckets[-1]
                buckets.pop()
            # [[], [3], [2], [1], [], []] --> []
            # [[], [3], [2], [1], []] --> []
            # [[], [3], [2], [1]] --> []
            # [[], [3], [2]] --> [1]
            # [[], [3]] --> [1, 2]

        return result
