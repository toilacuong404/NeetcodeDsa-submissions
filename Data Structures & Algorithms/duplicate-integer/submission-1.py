class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        for j in cnt:
            if cnt[j] >= 2:
                return True
        return False