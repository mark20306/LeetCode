class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        word.reverse()
        res = " ".join(word) #.strip()
        return res
