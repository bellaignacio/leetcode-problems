class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, val in enumerate(nums):
            complement = target - val

            if complement in hash:
                return [index, hash[complement]]
            
            hash[val] = index
