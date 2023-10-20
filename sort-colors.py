class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1

        i = 0
        for c in range(len(counts)):
            for x in range(counts[c]):
                nums[i] = c
                i += 1
