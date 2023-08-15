class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for i in s:
            if res and i == res[-1]:
                res.pop()
            else:
                res.append(i)    
        return "".join(res)