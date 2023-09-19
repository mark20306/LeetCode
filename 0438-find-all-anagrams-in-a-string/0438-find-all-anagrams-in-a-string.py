class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s): return []
        scount , pcount = [0] * 26 , [0] * 26
        for i in range(len(p)):
            pcount[ord(p[i]) - ord("a")] += 1
            scount[ord(s[i]) - ord("a")] += 1
        if pcount == scount:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            # 將右邊界的字符納入窗口
            scount[ord(s[r]) - ord("a")] += 1
            scount[ord(s[l]) - ord("a")] -= 1
            # 如果窗口大小等於 p 的長度，檢查是否找到了一個字母排列
            if pcount == scount:
                res.append(l+1)
                
            # 將左邊界的字符移出窗口
            
            l += 1
        return res
        
        