from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        for i in t:
            if i in dict1:
                dict1[i] -= 1 
            elif dict1[i] == 0:
                return False
                break
        for i in dict1:
            if dict1[i] != 0:
                return False
        return True
                
        