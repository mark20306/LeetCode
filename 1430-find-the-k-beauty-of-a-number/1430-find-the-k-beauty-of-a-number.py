class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        numstr = str(num)
        for i in range(len(numstr) - k + 1):
            if int(numstr[i:i+k]) != 0 and num % int(numstr[i:i+k]) == 0:
                res += 1
        return res