class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(re.sub("(\s+)"," ",s.strip()).split(" ")))        