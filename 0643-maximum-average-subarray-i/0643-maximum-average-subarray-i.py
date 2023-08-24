class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxnum = float('-inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if i >= k:
                 temp -= nums[i - k]
            if i >= k-1:
                maxnum = max(maxnum , temp)
        return maxnum/k