class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = 1
        for i in range(1, n):
            prefix *= nums[i -1] 
            ans[i] = prefix
        suffix = 1
        for j in range(n - 1, -1, -1):
            ans[j] = ans[j] * suffix
            suffix *= nums[j] 
        return ans
            