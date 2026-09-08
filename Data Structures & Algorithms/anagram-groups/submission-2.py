class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for word in strs:
            cnt = [0]*26
            for ch in word:
                cnt[ord(ch)-ord('a')] +=1
            key = tuple(cnt)
            if key not in ana_dict:
                ana_dict[key] = []
            ana_dict[key].append(word)
        return list(ana_dict.values())