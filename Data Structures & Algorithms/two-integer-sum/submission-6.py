class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in res:
                return [res[x], i]
            res[n] = i