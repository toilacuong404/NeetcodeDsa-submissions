class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            cnt = [0]*26
            for ch in w:
                x = ord(ch) - ord('a')
                cnt[x] += 1
            key = tuple(cnt)
            if key not in res:
                res[key] = []
            res[key].append(w)
        return list(res.values())