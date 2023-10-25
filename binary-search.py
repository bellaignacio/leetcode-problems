class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(left, right):
            if left > right:
                return -1

            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return recurse(left, mid - 1)
            elif target > nums[mid]:
                return recurse(left + 1, right)

        return recurse(0, len(nums) - 1)
