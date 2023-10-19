class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for n in nums_set:
            if n - 1 not in nums_set: # n is beginning of sequence
                length = 0
                while (n + length) in nums_set: # how far can we go?
                    length += 1
                max_length = max(max_length, length)

        return max_length
