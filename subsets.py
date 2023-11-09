class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = [] # building solution candidate

        def _backtrack(i):
            if i >= len(nums):
                results.append(subset.copy()) # candidate is viable, add to results
                return

            # YES, include nums[i]
            subset.append(nums[i])
            _backtrack(i + 1)
            subset.pop() # "backtrack": undo modification

            # NO, do not include nums[i]
            _backtrack(i + 1)

        _backtrack(0)
        return results
