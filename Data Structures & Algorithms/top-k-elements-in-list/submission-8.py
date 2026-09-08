class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in cnt:
                cnt[num] +=1
            else:
                cnt[num] =1
        for v, c in cnt.items():
            freq[c].append(v)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


            
        