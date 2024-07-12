class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        temp = 0
        for i, u in enumerate(s):
            if i >= k and s[i - k] in 'aeiou':
                temp -= 1
            if u in 'aeiou':
                temp += 1
                ans = max(ans, temp)
        return ans
            
                