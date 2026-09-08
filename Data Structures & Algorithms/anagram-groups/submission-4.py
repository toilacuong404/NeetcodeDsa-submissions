class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas_map = {}
        for word in strs:
            cnt = [0]*26
            for ch in word:
                x = ord(ch) - ord('a')
                cnt[x] += 1
            key = tuple(cnt)
            if key not in anas_map:
                anas_map[key] = []
            anas_map[key].append(word)
        return list(anas_map.values())