class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            other = target - n
            if other in num_map:
                return [num_map[other], i]
            num_map[n] = i
        return []