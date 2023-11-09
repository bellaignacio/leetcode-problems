class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = [] # building solution candidate

        def _backtrack(i):
            if i >= len(nums):
                results.append(subset.copy()) # candidate is valid, add to results
                return

            # YES, include nums[i]
            subset.append(nums[i]) # go down one level
            _backtrack(i + 1)
            subset.pop() # "backtrack": undo modification, go back up one level

            # NO, do not include nums[i]
            _backtrack(i + 1)

        _backtrack(0)
        return results
