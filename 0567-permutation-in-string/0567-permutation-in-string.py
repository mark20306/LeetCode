class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        s1count , s2count = [0] * 26 , [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        match = 0
        for i in range(26):
                match += 1 if s1count[i] == s2count[i] else 0

        l = 0
        for r in range(len(s1) , len(s2)):
            if match == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2count[index] += 1
            if s2count[index] == s1count[index]:
                match += 1
            elif s2count[index] == s1count[index] + 1:
                match -= 1

            index = ord(s2[l]) - ord("a")
            s2count[index] -= 1
            if s2count[index] == s1count[index]:
                match += 1
            elif s2count[index] == s1count[index] - 1:
                match -= 1

            l += 1
        return match == 26


        