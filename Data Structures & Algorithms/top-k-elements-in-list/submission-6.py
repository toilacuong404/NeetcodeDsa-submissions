class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in cnt:
                cnt[i] = 1
            else: cnt[i] += 1
        for key, fre in cnt.items():
            freq[fre].append(key)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        