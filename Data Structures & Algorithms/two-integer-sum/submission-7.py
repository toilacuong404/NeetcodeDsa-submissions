class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, num in enumerate(nums):
            x = target - num
            if x in res:
                return [res[x], index]
            res[num] = index