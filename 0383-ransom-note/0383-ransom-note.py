class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht = {}
        for n in magazine:
            if n in ht:
                ht[n] += 1
            else:
                ht[n] = 1

        for c in ransomNote:
            if c in ht and ht[c] >= 1:
                ht[c] -= 1
            else:
                return False
        return True