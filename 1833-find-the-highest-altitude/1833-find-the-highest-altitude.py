class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, temp = 0, 0
        for i in gain:
            temp += i
            ans = max(ans, temp)
        return ans