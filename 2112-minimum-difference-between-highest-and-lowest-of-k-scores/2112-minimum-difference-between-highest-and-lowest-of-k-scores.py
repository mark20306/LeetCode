class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        res = float("inf")
        nums.sort()
        l = 0
        for r in range(k - 1 , len(nums)):
            res = min(res , nums[r] - nums[l])
            l += 1
        return res
