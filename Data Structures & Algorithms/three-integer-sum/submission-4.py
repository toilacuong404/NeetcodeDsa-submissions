class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(0, len(nums)-2):
            if x>0 and nums[x] == nums[x-1]:
                continue
            target = -nums[x]
            i, j = x+1, len(nums)-1
            while i < j:
                two_sum = nums[i] + nums[j]
                if two_sum < target:
                    i += 1
                elif two_sum > target:
                    j -=1
                else:
                    res.append([nums[i], nums[j] , nums[x]])
                    while i < j and nums[i] == nums[i+1]:
                        i +=1
                    i+= 1
                    j -=1
        return res