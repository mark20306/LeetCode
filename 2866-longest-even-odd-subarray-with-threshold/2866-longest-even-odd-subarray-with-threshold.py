class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <=threshold:
                curr = 1
                res = max(res , curr)
                while i + 1 < len(nums) and nums[i] % 2 != nums[i + 1] % 2 and nums[i+1] <=threshold:
                    curr += 1
                    res = max(res , curr)
                    i += 1
            else:
                curr = 0
        return res