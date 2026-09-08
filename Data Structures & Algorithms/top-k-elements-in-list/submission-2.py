class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums)+1)]
        for j in nums:
            if j not in cnt:
                cnt[j] = 1
            else:
                cnt[j] += 1
        for num, c in cnt.items():
            freq[c].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

