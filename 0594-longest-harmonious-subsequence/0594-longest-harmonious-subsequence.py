class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num = Counter(nums)
        ans = 0
        for i in num:
            if i + 1 in num:
                ans = max(ans , num[i] + num[i + 1])
        return ans
