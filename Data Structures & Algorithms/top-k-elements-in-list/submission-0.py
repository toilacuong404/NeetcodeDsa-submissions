class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        result = []
        for i in nums:
            if i not in cnt:
                cnt[i] =1
            else: cnt[i] += 1
        sort_items = sorted(cnt.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            result.append(sort_items[i][0])
        return result

