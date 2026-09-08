class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in res:
                return [res[x], i]
            res[nums[i]] = i            