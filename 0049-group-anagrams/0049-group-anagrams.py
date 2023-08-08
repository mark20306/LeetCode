class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        if len(strs) < 1:
            return strs
        else:   
            for i in range(len(strs)):
                reg = strs[i]
                regsort = "".join(sorted(reg))
                if regsort in hashmap:
                    hashmap[regsort].append(reg)
                else:
                    hashmap[regsort] = [reg]
                
        return hashmap.values()                     
            