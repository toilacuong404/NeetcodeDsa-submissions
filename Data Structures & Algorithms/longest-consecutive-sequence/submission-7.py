class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        if len(nums) == 0:
            return 0
        else:
            temp = []
            res = 1
            for i in range(1, len(a)):
                if abs(a[i-1] - a[i]) == 1:
                    res += 1
                else:
                    temp.append(int(res))
                    res = 1
            temp.append(res)
            return max(temp)


        
