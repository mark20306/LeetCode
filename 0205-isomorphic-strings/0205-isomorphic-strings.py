class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if t[i] != hashmap[s[i]]:    
                    return False
            else:
                if t[i] not in hashmap.values():
                    hashmap[s[i]] = t[i]
                else:
                    return False
        return True