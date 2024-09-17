class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i -1] 
            ans[i] = prefix
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] = ans[j] * suffix
            suffix *= nums[j] 
        return ans
            