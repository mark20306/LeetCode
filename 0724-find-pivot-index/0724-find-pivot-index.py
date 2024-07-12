class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            totalSum = sum(nums)
            leftSum = 0

            for i, u in enumerate(nums):
                if leftSum == totalSum - u - leftSum:
                    return i
                leftSum += u
            return -1


        