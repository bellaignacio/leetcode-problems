class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = ((right - left) // 2) + left
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def _search(left, right):
            if left == right:
                return left

            mid = ((right - left) // 2) + left
            if nums[mid + 1] > nums[mid]:
                return _search(mid + 1, right)
            else:
                return _search(left, mid)

        return _search(0, len(nums) - 1)
