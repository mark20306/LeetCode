class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        s1count , s2count = [0] * 26 , [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        if s1count == s2count:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            # 將右邊界的字符納入窗口
            s2count[ord(s2[r]) - ord("a")] += 1
            # 將左邊界的字符移出窗口
            s2count[ord(s2[l]) - ord("a")] -= 1
            # 如果窗口大小等於 p 的長度，檢查是否找到了一個字母排列
            if s1count == s2count:
                return True
                
            
            
            l += 1
        return False


        