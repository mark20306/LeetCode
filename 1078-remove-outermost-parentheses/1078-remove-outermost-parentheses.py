class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        for i in s:
            if i == "(":
                if opened > 0:
                    res.append(i)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    res.append(i)    
        return "".join(res)