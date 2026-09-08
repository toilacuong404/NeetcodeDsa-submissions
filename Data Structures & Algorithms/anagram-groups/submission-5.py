class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_maps = {}
        for w in strs:
            cnt = [0]*26
            for ch in w:
                x = ord(ch)-ord('a')
                cnt[x] += 1
            key = tuple(cnt)
            if key not in ana_maps:
                ana_maps[key] = []
            ana_maps[key].append(w)
        return list(ana_maps.values())
            

            
            