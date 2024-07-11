class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        ans = 0
        sort_g = sorted(g)
        sort_s = sorted(s)
        while i < len(g) and j < len (s):
            if sort_s[j] >= sort_g[i]:
                ans += 1
                i += 1
            j += 1
        return ans
        