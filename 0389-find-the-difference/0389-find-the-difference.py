class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Map = {}
        for i in s:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i] += 1
        
        for c in t:
            if c in Map and Map[c] > 0:
                Map[c] -= 1
            else:
                return c
