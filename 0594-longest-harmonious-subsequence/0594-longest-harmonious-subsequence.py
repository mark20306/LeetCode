class Solution:
    def findLHS(self, nums: List[int]) -> int:
        Map = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in Map:
                Map[nums[i]] = 1
            else:
                Map[nums[i]] += 1
        if len(Map) <= 1:
            return 0
        for k in Map:
            if k + 1 in Map:
                ans = max(ans , Map[k] + Map[k + 1])
        return ans
