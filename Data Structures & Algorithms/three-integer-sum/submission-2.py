class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for x in range(0, len(nums)-2):
            target = -nums[x]
            if x > 0 and nums[x] == nums[x-1]:
                continue
            i, j = x+1, len(nums)-1
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    res.append([nums[x], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif s > target:
                    j -= 1
                elif s < target:
                    i += 1
        return res
        