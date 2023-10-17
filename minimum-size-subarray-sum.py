class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target: # want total < target to shorten subarray - want to find minimal subarray
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
